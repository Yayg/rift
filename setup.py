#! /usr/bin/env python2

from setuptools import setup, find_packages

class TestCommand():
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("BIT")

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
        'termcolor',
        'colorama'
    ],

    test_suite="tests",

    zip_safe=False
)
