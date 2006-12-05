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

import lxml.etree

import zope.testbrowser.testing


html_parser = lxml.etree.HTMLParser()


class EtreeTestBrowser(zope.testbrowser.testing.Browser):
    """A testbrowser derivation that offers its content 
    also as an etree.

    """

    @property
    def etree(self):
        if self._etree is not None:
            return self._etree
        self._etree = etree.parse(self.contents, html_parser)
        return self._etree

    def _changed(self):
        super(EtreeTestBrowser, self)._changed()
        self._etree = None
