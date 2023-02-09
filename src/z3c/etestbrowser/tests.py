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
"""Testing z3c.etestbrowser."""

import doctest
import os.path
import unittest

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

import z3c.etestbrowser


class Layer(zope.testbrowser.wsgi.TestBrowserLayer,
            zope.app.wsgi.testlayer.BrowserLayer):
    """Layer to prepare zope.testbrowser using the WSGI app."""


wsgi_layer = Layer(
    z3c.etestbrowser,
    zcml_file=os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    allowTearDown=True)


def setUpWSGI(test):
    test.globs['wsgi_app'] = wsgi_layer.make_wsgi_app()


def test_suite():
    suite = unittest.TestSuite()

    wsgi_test = doctest.DocFileSuite(
        "README.rst",
        "over_the_wire.rst",
        "wsgi.rst",
        setUp=setUpWSGI,
        optionflags=(
            doctest.NORMALIZE_WHITESPACE
            | doctest.ELLIPSIS
            | doctest.IGNORE_EXCEPTION_DETAIL))
    wsgi_test.layer = wsgi_layer
    suite.addTest(wsgi_test)
    return suite
