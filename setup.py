

from setuptools import setup


setup(
    name='my_plugin',
    version = '0.1.0',
    description = 'A pytest plguin to greet you in the Shona language before you run your tests',
    url='https://wherever/you/have/info/on/this/package',
    author = 'Tim Chen',
    author_email='cct823@gmail.com',
    license ='proprietary',
    py_modules=['my_plugin'],
    install_requires = ['pytest'],
    entry_points = {'pytest11':['greeting = my_plugin']}
)

