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

import doctest
import os.path
import unittest

from zope.app.testing import functional


layer = functional.ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'ETestBrowserLayer')


def test_suite():
    suite = unittest.TestSuite()
    test = functional.FunctionalDocFileSuite(
        "README.txt",
        "over_the_wire.txt",
        optionflags=doctest.REPORT_NDIFF|doctest.NORMALIZE_WHITESPACE|
        doctest.ELLIPSIS)
    test.layer = layer
    suite.addTest(test)
    return suite
