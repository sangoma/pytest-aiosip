import os
import re

from setuptools import setup


with open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'pytest_aiosip', '__init__.py'), 'r') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(
    name='pytest-aiosip',
    version=version,
    description=('pytest plugin for aiosip support'),
    long_description=read('README.rst'),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
        'Framework :: Pytest',
        'Framework :: AsyncIO',
    ],
    author='Simon Gomizelj',
    author_email='simon@vodik.xyz',
    url='https://github.com/vodik/pytest-aiosip/',
    license='Apache 2',
    install_requires=[
        'pytest',
        'aiosip>=0.2.0'
    ],
    packages=['pytest_aiosip'],
    entry_points={
        'pytest11': ['aiosip = pytest_aiosip'],
    },
)
