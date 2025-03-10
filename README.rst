.. caution::

    This repository is no longer maintained and thus it got archived.

    If you want to work on it please open a ticket in
    https://github.com/zopefoundation/meta/issues requesting its unarchival.

=====================================
Extensions for the Zope 3 testbrowser
=====================================

This package is intended to provide extended versions of the Zope 3
testbrowser_. Especially those extensions that introduce dependencies to more
external products, like lxml.

.. _testbrowser: https://pypi.org/project/zope.testbrowser/

.. contents::

Extension: lxml-support
=======================

All HTML pages are parsed and provided as an element-tree.
