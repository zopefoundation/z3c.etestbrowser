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
import re
import unittest

import z3c.etestbrowser
import zope.app.wsgi.testlayer
import zope.testing.renormalizing

try:
    ascii
except NameError:
    # Python 2
    ascii = repr


try:
    unichr
except NameError:
    # Python 3
    unichr = chr


checker = zope.testing.renormalizing.OutputChecker([
    # Python 3 prints uncode reprs differently
    (re.compile(r"\bu('[^']*')"), r'\1'),
    # Python 3 prints fully-qualified dotted names for exceptions
    (re.compile(r'lxml\.etree\.(XMLSyntaxError:)'), r'\1'),
    (re.compile(r'zope\.testbrowser\.browser\.(RobotExclusionError:)'), r'\1'),
    # Python 2's formatter treat NBSP as printable characters,
    # Python 3's formatter treats NBSP as a space and normalizes it
    (re.compile(unichr(0xA0)), r' '),
])


wsgi_layer = zope.app.wsgi.testlayer.BrowserLayer(z3c.etestbrowser,
                                                  allowTearDown=True)


def setUpWSGI(test):
    test.globs['wsgi_app'] = wsgi_layer.make_wsgi_app()
    test.globs['ascii'] = ascii


def test_suite():
    suite = unittest.TestSuite()
    wsgi_test = doctest.DocFileSuite(
        "README.txt",
        "over_the_wire.txt",
        setUp=setUpWSGI,
        checker=checker,
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
    wsgi_test.layer = wsgi_layer
    suite.addTest(wsgi_test)
    return suite
