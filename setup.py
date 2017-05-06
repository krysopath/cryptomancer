#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup
setup(
    name='cryptomancer',
    version='0.1.1',
    description='cryptomancer module, contains crypto related helpers',
    author='Georg',
    author_email='krysopath@gmail.com',
    url='ssh://git@endtropie.mooo.com:22222/home/git/cryptomancer.git',
    packages=['cryptomancer'],
    install_requires=['gnupg']
)