#! /usr/bin/env python2

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
        'ctypes',
    ],

    zip_safe=False
)