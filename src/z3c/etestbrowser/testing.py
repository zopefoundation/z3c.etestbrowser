##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Extensions for z3c.etestbrowser

$Id$
"""

import re
import StringIO
import htmllib
import formatter

import lxml.etree

import zope.testbrowser.testing


RE_CHARSET = re.compile('.*;charset=(.*)')


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + "  "
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


class ExtendedTestBrowser(zope.testbrowser.testing.Browser):
    """An extended testbrowser implementation.

    Features:

        - offers the content also as parsed etree

    """

    xml_strict = False
    normalized_contents = ''

    _etree = None

    @property
    def etree(self):
        if self._etree is not None:
            return self._etree
        # I'm not using any internal knowledge about testbrowser
        # here, to avoid breakage. Memory usage won't be a problem.
        if self.xml_strict:
            self._etree = lxml.etree.XML(self.contents)
        else:
            # This is a workaround against the broken fallback for 
            # encoding detection of libxml2.
            # We have a chance of knowing the encoding as Zope states this in
            # the content-type response header.
            content = self.contents
            content_type = self.headers['content-type']
            match = RE_CHARSET.match(content_type)
            if match is not None:
                charset = match.groups()[0]
                content = content.decode(charset)
            self._etree = lxml.etree.HTML(content)

        return self._etree

    def _changed(self):
        super(ExtendedTestBrowser, self)._changed()
        self._etree = None
        tree = self.etree
        indent(tree)
        self.normalized_contents = lxml.etree.tostring(tree, pretty_print=True)

    def pretty_print(self):
        """Print a pretty (formatted) version of the HTML content.

        If the content is not text/html then it is just printed.
        """
        if not self.headers['content-type'].lower().startswith('text/html'):
            print self.contents
        else:
            parser = htmllib.HTMLParser(
                formatter.AbstractFormatter(formatter.DumbWriter()))
            parser.feed(self.contents)
            parser.close()
