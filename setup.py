

from setuptools import setup


setup(
    name='Service-Uno',
    version = '0.1.0',
    description = 'A pytest plguin to greet you in the ASCII language before you run your tests',
    url='https://wherever/you/have/info/on/this/package',
    author = 'Service-Uno',
    author_email='Service-Uno@cgu.edu',
    license ='proprietary',
    py_modules=['my_plugin'],
    install_requires = [''],
    # entry_points = {'pytest11':['greeting = my_plugin']}
)


