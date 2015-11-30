#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ripe',
    version='0.1',
    description='ripe is partially eponym',
    url='incoming',

    author='Rafael \'yayg\' Gozlan',
    author_email='rafael.gozlan@epita.fr',

    license = "MIT",

    packages=['ripe'],
    install_requires=[
        'termcolor',
        'colorama'
    ],

    use_2to3 = True,

    zip_safe=False
)
