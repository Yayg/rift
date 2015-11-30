#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='rift',
    version='0.1',
    description='rift is partially eponym',
    url='incoming',

    author='Rafael \'yayg\' Gozlan',
    author_email='rafael.gozlan@epita.fr',

    license = "MIT",

    packages=['rift'],
    install_requires=[
        'termcolor',
        'colorama'
    ],

    use_2to3 = True,

    zip_safe=False
)
