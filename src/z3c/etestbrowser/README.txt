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
  <Element html at ...>
  >>> browser.etree.xpath('//body')
  [<Element body at ...>]


Strict XML
==========

It is possible to force the test browser to use the xml parser::

  >>> browser.xml_strict
  False
  >>> browser.xml_strict = True
  >>> browser.open("http://localhost/")
  >>> browser.etree
  <Element {http://www.w3.org/1999/xhtml}html at ...>
  >>> browser.etree.xpath(
  ...     '//html:body', {'html': 'http://www.w3.org/1999/xhtml'})
  [<Element {http://www.w3.org/1999/xhtml}body at ...>]

LXML unicode support
====================

A couple of variations of libxml2 might interpret UTF-8 encoded strings
incorrectly. We have a workaround for that. Let's have a look at a view that
contains a German umlaut:

  >>> browser.xml_strict = False
  >>> browser.open('http://localhost/lxml.html')
  >>> browser.etree.xpath("//span")[0].text
  u'K\xfcgelblitz.'
