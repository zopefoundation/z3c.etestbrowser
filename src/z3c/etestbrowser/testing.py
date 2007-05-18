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

import StringIO
import lxml.etree

import zope.testbrowser.testing


html_parser = lxml.etree.HTMLParser()


class ExtendedTestBrowser(zope.testbrowser.testing.Browser):
    """An extended testbrowser implementation.

    Features:

        - offers the content also as parsed etree

    """

    xml_strict = False

    _etree = None

    @property
    def etree(self):
        if self._etree is not None:
            return self._etree
        # I'm not using any internal knowledge about testbrowser
        # here, to avoid breakage. Memory usage won't be a problem.
        if self.xml_strict:
            parser = None
        else:
            parser = html_parser
        self._etree = lxml.etree.XML(self.contents, parser)
        return self._etree

    def _changed(self):
        super(ExtendedTestBrowser, self)._changed()
        self._etree = None
