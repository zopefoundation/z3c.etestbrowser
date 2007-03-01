====================
Extended testbrowser
====================

This package provides some extensions to Zope 3's testbrowser. It is intended
for extensions that have dependencies that we do not want to rely on in the
  Zope 3 core e.g. lxml.

Requirements
============

 - lxml

EtreeTestBrowser
================

EtreeTestBrowser parses the result of a request into an etree using lxml (if
it's text/html or text/xml).

Useful to perform more detailed analysis of web pages using e.g. XPath and
related XML technologies.

Example::

  >>> from z3c.etestbrowser.testing import ExtendedTestBrowser
  >>> browser = ExtendedTestBrowser()
  >>> browser.open("http://localhost/")
  >>> print browser.contents
  <!DOCTYPE ...>
  ...
  </html>
  >>> browser.etree
  <etree._ElementTree object at 0x...>
  >>> browser.etree.xpath('//html')
  [<Element html at ...>]
