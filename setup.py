from setuptools import setup, find_packages

setup(
    name='z3c.etestbrowser',
    version='trunk',
    author='Christian Theune',
    author_email='ct@gocept.com',
    url='svn://svn.zope.org/repos/main/z3c.etestbrowser',
    description="""\
Extensions for zope.testbrowser.
""",
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    license='ZPL 2.1',

    install_requires=['setuptools',
                      'lxml'
                     ],
)
