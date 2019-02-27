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
import zope.deferredimport
zope.deferredimport.initialize()

zope.deferredimport.deprecated(
    "z3c.etestbrowser.testing.ExtendedTestBrowser now speaks WSGI, so please "
    "use it. This BBB import will go away in Version 4.0.",
    Browser='z3c.etestbrowser:testing.ExtendedTestBrowser',
    ExtendedTestBrowser='z3c.etestbrowser:testing.ExtendedTestBrowser',
)
