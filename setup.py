# coding: utf-8
import sys
from setuptools import setup, find_packages


def README():
    with open('README.rst') as f:
        return f.read()


# Backward-compatibility dependencies for Python 2
_python2_requires = [
    'backports.os',
    'future',  # For backport of surrogateescape
] if sys.version_info < (3,) else []


setup(
    name='backports.test.support',
    description="Backport of Python 3's test.support package",
    long_description=README(),
    url='https://github.com/pjdelport/backports.test.support',

    author='Pi Delport',
    author_email='pjdelport@gmail.com',

    package_dir={'': 'src'},
    packages=find_packages('src'),

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    install_requires=_python2_requires,

    license='Python Software Foundation License',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
