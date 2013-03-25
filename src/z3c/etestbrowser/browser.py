##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
"""Extensions for z3c.etestbrowser"""

import formatter
import re

import lxml.etree
import lxml.html

import zope.testbrowser.browser

try:
    from htmllib import HTMLParser
except ImportError:
    # Python 3
    from ._prettyprint import HTMLParser


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


class ExtendedTestBrowser(zope.testbrowser.browser.Browser):
    """An extended testbrowser implementation.

    Features:

        - offers the content also as parsed etree

    """

    xml_strict = False

    _etree = None
    _normalized_contents = None

    @property
    def etree(self):
        if self._etree is not None:
            return self._etree
        # I'm not using any internal knowledge about testbrowser
        # here, to avoid breakage. Memory usage won't be a problem.
        if self.xml_strict:
            self._etree = lxml.etree.fromstring(
                self.contents,
                parser=lxml.etree.XMLParser(resolve_entities=False))
        else:
            content = self.contents
            if isinstance(content, bytes):
                content_type = self.headers['content-type']
                match = RE_CHARSET.match(content_type)
                if match is not None:
                    charset = match.groups()[0].strip('"' + "'")
                    content = content.decode(charset)
            self._etree = lxml.etree.HTML(content)

        return self._etree

    @property
    def normalized_contents(self):
        if self._normalized_contents is None:
            indent(self.etree)
            self._normalized_contents = lxml.etree.tostring(
                self.etree, pretty_print=True).decode('UTF-8')
        return self._normalized_contents

    def _changed(self):
        super(ExtendedTestBrowser, self)._changed()
        self._etree = None
        self._normalized_contents = None

    def pretty_print(self):
        """Print a pretty (formatted) version of the HTML content.

        If the content is not text/html then it is just printed.
        """
        if not self.headers['content-type'].lower().startswith('text/html'):
            print(self.contents)
        else:
            parser = HTMLParser(
                formatter.AbstractFormatter(formatter.DumbWriter()))
            parser.feed(self.contents)
            parser.close()
