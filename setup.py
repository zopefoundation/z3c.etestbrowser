from setuptools import setup, find_packages

setup(
    name='z3c.etestbrowser',
    version='1.0.3',
    author='Christian Theune',
    author_email='ct@gocept.com',
    url='http://svn.zope.org/z3c.etestbrowser/trunk/',
    description="""\
Extensions for zope.testbrowser.
""",
    long_description = open('README.txt').read(),
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    license='ZPL 2.1',
    extras_require=dict(test=['zope.app.testing', 'zope.app.zcmlfiles',
                              'zope.app.securitypolicy', 'zope.app.server']),
    install_requires=['setuptools',
                      'lxml<2.0-dev',
                      'zope.testbrowser'
                     ],
)
