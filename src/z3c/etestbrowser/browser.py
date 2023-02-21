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
"""Extensions for z3c.etestbrowser."""

import re

import lxml.etree
import lxml.html
import zope.testbrowser.browser


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
            # This is a workaround against the broken fallback for
            # encoding detection of libxml2.
            # We have a chance of knowing the encoding as Zope states this in
            # the content-type response header.
            self._etree = lxml.etree.HTML(self.contents)

        if self._etree is None:
            raise ValueError(
                'ETree could not be constructed. Contents might be empty.')
        return self._etree

    @property
    def normalized_contents(self):
        if self._normalized_contents is None:
            indent(self.etree)
            self._normalized_contents = lxml.etree.tostring(
                self.etree, pretty_print=True, encoding=str)
        return self._normalized_contents

    def _changed(self):
        super()._changed()
        self._etree = None
        self._normalized_contents = None
