from setuptools import setup , find_packages


setup(
    name='Service-Uno',
    version = '1.2.0',
    description = 'Service rating program',
    url='https://github.com/cct823/Service-Uno',
    author = 'Service-Uno',
    author_email='Service-Uno@cgu.edu',
    license ='proprietary',
    py_modules=['serviceuno'],
    install_requires = [''],
    packages = find_packages(where='Source'),
    package_dir = {'':'Source'}
    # entry_points = {'pytest11':['greeting = my_plugin']}
)


