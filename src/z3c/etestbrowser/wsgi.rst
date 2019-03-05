Deprecated special support for zope.testbrowser.wsgi
----------------------------------------------------

There was also a variant in ``z3c.etestbrowser.wsgi`` which could be used for
the WSGI variant of ``zope.testbrowser``. It is no longer necessary because.
``z3c.etestbrowser.testing`` now speaks WSGI. It will be removed in the next
major release.

Example:

  >>> import z3c.etestbrowser.wsgi
  >>> browser = z3c.etestbrowser.wsgi.Browser(wsgi_app=wsgi_app)
  >>> browser.open("http://localhost/")
  >>> print(browser.contents)
  <!DOCTYPE ...>
  ...
  </html>
  >>> browser.etree
  <Element html at ...>
  >>> browser.etree.xpath('//body')
  [<Element body at ...>]

