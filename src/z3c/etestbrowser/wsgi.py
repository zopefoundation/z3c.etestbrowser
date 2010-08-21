##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
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
"""z3c.etestbrowser for zope.app.wsgi.testlayer."""

import z3c.etestbrowser.browser
import zope.app.wsgi.testlayer


class ExtendedTestBrowser(zope.app.wsgi.testlayer.Browser,
                          z3c.etestbrowser.browser.ExtendedTestBrowser):
    """An extended testbrowser implementation.

    Based on zope.app.wsgi.testlayer.Browser.

    """
