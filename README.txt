Extensions for the Zope 3 testbrowser
=====================================

This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to more
external products, like lxml.

Changes
-------

1.0.3
~~~~~

- Remedy brown-bag 1.0.2-release: Someone already released 1.0.2-r* instead of
  a .dev release making the 1.0.2 final too old. :/

1.0.2
~~~~~

- Helping libxml2 with some encoding guesswork.

Extension: lxml-support
-----------------------

All HTML pages are parsed and provided as an element-tree.
