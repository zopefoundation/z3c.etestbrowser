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
"""Setup for z3c.etestbrowser package."""

import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(*rnames)) as f:
        return f.read()


test_requires = [
    'zope.annotation',
    'zope.app.appsetup',
    'zope.app.publication',
    'zope.app.wsgi[testlayer] >= 4.0dev',
    'zope.authentication',
    'zope.browserpage',
    'zope.component',
    'zope.container',
    'zope.location',
    'zope.principalregistry',
    'zope.publisher',
    'zope.security',
    'zope.securitypolicy',
    'zope.site',
    'zope.testbrowser[test]',
    'zope.testing',
    'zope.testrunner',
    'zope.traversing',
]

setup(name='z3c.etestbrowser',
      version='4.0',
      author='Christian Theune',
      author_email='zope-dev@zope.dev',
      description='Extensions for zope.testbrowser',
      long_description=(
          read('README.rst') + '\n\n' +
          read('src', 'z3c', 'etestbrowser', 'README.rst') + '\n\n' +
          read('src', 'z3c', 'etestbrowser', 'over_the_wire.rst') + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="zope3 testbrowser lxml",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='https://github.com/zopefoundation/z3c.etestbrowser',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['z3c'],
      python_requires='>=3.7',
      extras_require={
          "test": test_requires,
      },
      install_requires=[
          'lxml >= 2.2',
          'setuptools',
          'zope.deferredimport',
          'zope.testbrowser >= 5.0',
      ],
      include_package_data=True,
      zip_safe=False,
      )
