Extended testbrowser
--------------------

This package provides some extensions to ``zope.testbrowser``.  These are not
included in the core because they have extra dependencies, such as ``lxml``.


Requirements
~~~~~~~~~~~~

 - lxml


etree support
~~~~~~~~~~~~~

The extended test browser allows parsing of the result of a request into an
etree using lxml (if the content type is text/html or text/xml).

This is useful to perform more detailed analysis of web pages using e.g. XPath
and related XML technologies.

Example:

  >>> from z3c.etestbrowser.testing import ExtendedTestBrowser
  >>> browser = ExtendedTestBrowser()
  >>> browser.open("http://localhost/")
  >>> print(browser.contents)
  <!DOCTYPE ...>
  ...
  </html>
  >>> browser.etree
  <Element html at ...>
  >>> browser.etree.xpath('//body')
  [<Element body at ...>]


Strict XML
++++++++++

It is possible to force the test browser to use the xml parser:

  >>> browser.xml_strict
  False
  >>> browser.xml_strict = True
  >>> browser.open("http://localhost/")
  >>> browser.etree
  <Element {http://www.w3.org/1999/xhtml}html at ...>
  >>> browser.etree.xpath(
  ...     '//html:body', namespaces={'html': 'http://www.w3.org/1999/xhtml'})
  [<Element {http://www.w3.org/1999/xhtml}body at ...>]

LXML unicode support
++++++++++++++++++++

A couple of variations of libxml2 might interpret UTF-8 encoded strings
incorrectly. We have a workaround for that. Let's have a look at a view that
contains a German umlaut:

  >>> browser.xml_strict = False
  >>> browser.open('http://localhost/lxml.html')
  >>> browser.etree.xpath("//span")[0].text == u'K\xfcgelblitz.'
  True

Invalid XML/HTML responses
++++++++++++++++++++++++++

Responses that contain a body with invalid XML/HTML will cause an error when
accessing the etree or normalized_contents attribute, but will load fine for
general TestBrowser use:

  >>> browser.open("http://localhost/empty.html")
  >>> browser.contents
  ''
  >>> browser.etree
  Traceback (most recent call last):
  ValueError: ...
  >>> browser.normalized_contents
  Traceback (most recent call last):
  ValueError: ...


HTML/XML normalization
~~~~~~~~~~~~~~~~~~~~~~

The extended test browser allows normalized output of HTML and XML which makes
testing examples with HTML or XML a bit easier when unimportant details like
whitespace are changing:

  >>> browser.open('http://localhost/funny.html')
  >>> print(browser.contents)
  <html>
    <head>
      <title>Foo</title>
  </head>
      <body>
            <h1>
        Title
      </h1>
          </body>
              </html>
  <BLANKLINE>

versus

  >>> print(browser.normalized_contents)
  <html>
    <head>
      <title>Foo</title>
    </head>
    <body>
      <h1>
        Title
      </h1>
    </body>
  </html>
