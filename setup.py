##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for z3c.viewlet package

$Id$
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='z3c.etestbrowser',
      version = '1.4.1dev',
      author='Christian Theune',
      author_email='ct@gocept.com',
      description='Extensions for zope.testbrowser',
      long_description=(
          read('README.txt')
          + '\n\n' +
          read('src', 'z3c', 'etestbrowser', 'README.txt')
          + '\n\n' +
          read('src', 'z3c', 'etestbrowser', 'over_the_wire.txt')
          + '\n\n' +
          read('CHANGES.txt')
          ),
      keywords = "zope3 testbrowser lxml",
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      url='http://cheeseshop.python.org/pypi/z3c.etestbrowser',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['z3c'],
      extras_require=dict(test=['zope.app.testing',
                                'zope.app.zcmlfiles',
                                'zope.app.securitypolicy',
                                'zope.app.server',
                                'zope.testbrowser[test]',
                                ]),
    install_requires=['setuptools',
                      'lxml>=2.2',
                      'zope.testbrowser'
                     ],
      include_package_data = True,
      zip_safe = False,
      )
