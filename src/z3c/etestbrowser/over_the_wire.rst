Using testbrowser on the internet
---------------------------------

The ``z3c.etestbrowser.browser`` module exposes an ``ExtendedTestBrowser``
class that simulates a web browser similar to Mozilla Firefox or IE.

    >>> from z3c.etestbrowser.browser import ExtendedTestBrowser
    >>> browser = ExtendedTestBrowser()

It can send arbitrary headers; this is helpful for setting the language value,
so that your tests format values the way you expect in your tests, if you rely
on zope.i18n locale-based formatting or a similar approach.

    >>> browser.addHeader('Accept-Language', 'en-US')

The browser can `open` web pages:

    >>> browser.open('https://www.w3.org')
    >>> print(browser.contents)
    <!doctype html>
    ...<h1>Making the Web work</h1>...
