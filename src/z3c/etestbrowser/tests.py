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
"""Testing for z3c.etestbrowser

$Id$
"""

from zope.app.testing import functional
import doctest
import os.path
import unittest
import z3c.etestbrowser
import zope.app.wsgi.testlayer


layer = functional.ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'ETestBrowserLayer')

wsgi_layer = zope.app.wsgi.testlayer.BrowserLayer(z3c.etestbrowser)

def test_suite():
    suite = unittest.TestSuite()

    test = functional.FunctionalDocFileSuite(
        "README.txt",
        "over_the_wire.txt",
        optionflags=doctest.REPORT_NDIFF|doctest.NORMALIZE_WHITESPACE|
        doctest.ELLIPSIS)
    test.layer = layer
    suite.addTest(test)

    wsgi_test = doctest.DocFileSuite(
        "wsgi.txt",
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
    wsgi_test.layer = wsgi_layer
    suite.addTest(wsgi_test)
    return suite
