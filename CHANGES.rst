=======
CHANGES
=======

4.0 (2023-02-21)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.8, 3.9, 3.10, 3.11.

- Drop deprecated support for ``python setup.py test``.

- Drop deprecated ``z3c.etestbrowser.wsgi``.


3.0.1 (2019-03-05)
==================

- Fix deprecation declaration in ``.wsgi``.


3.0 (2019-03-04)
================

Backwards incompatible changes
------------------------------

- Add support for ``zope.testbrowser >= 5.0`` which speaks WSGI this requires
  tests to be updated to WSGI.

- Deprecate ``z3c.etestbrowser.wsgi`` which used to contain the WSGI variant
  as it is now the default.

- Drop the ``zope.app.testing`` extra introduced in version 2.0.0 as
  it dropped its special ``zope.testbrowser`` support.

- Drop ``.browser.ExtendedTestBrowser.pretty_print`` as its requirements are
  deprecated or even removed from Python's StdLib.

- Adapt the code to newer ``lxml`` versions which no longer raise an exception
  if the string to be parsed by ``lxml.etree`` is empty. We now raise a
  ``ValueError`` in this case.

Features
--------

- Add support for Python 3.6 up to 3.7.


2.0.1 (2015-11-09)
==================

- Fix `over_the_wire.txt`


2.0.0 (2011-10-13)
==================

- No longer depending on ``zope.app.wsgi`` but on ``zope.testbrowser`` >= 4.0
  for the WSGI flavor of testbrowser.

- Added a `zope.app.testing` extra. You should use this extra if you want to
  use the browser in ``z3c.etestbrowser.testing``. (The base testbrowser used
  there has been moved from ``zope.testbrowser`` to ``zope.app.testing`` in
  version 4.0.)

- Renamed ``z3c.etestbrowser.wsgi.ExtendedTestBrowser`` to ``Browser`` for
  equality with ``zope.testbrowser`` but kept ``ExtendedTestBrowser`` for
  backwards compatibility.

1.5.0 (2010-08-22)
==================

- Added ``z3c.etestbrowser.wsgi.ExtendedTestBrowser``, a variant that can be
  used when the test layer was set up using ``using
  zope.app.wsgi.testlayer``.


1.4.0 (2010-07-08)
==================

- Took ``zope.securitypolicy`` refactoring and ``zope.testing.doctest``
  deprecation into account.

- Added ``z3c.etestbrowser.browser.ExtendedTestBrowser``, a variant that
  speaks HTTP instead of directly talking to the publisher talks to the
  publisher, see `Using testbrowser on the internet`_.


1.3.1 (2010-01-18)
==================

- Added doctest to `long_description` to show up on pypi.

1.3.0 (2009-07-23)
==================

- Updgraded pacakge to lxml 2.2.

- Fixed bug with `normalized_contents` which would break the `open` function
  of test browser if content wasn't parsable as HTML/XML.

1.2.0 (2008-05-29)
==================

- Added `normalized_contents` attribute that reindents and normalizes the
  etree structure of a document and allows easier to read HTML/XML examples in
  doctests.
