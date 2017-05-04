#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup
setup(
    name='safe',
    version='0.1.1',
    description='safe module, contains crypto related helpers',
    author='Georg',
    author_email='krysopath@gmail.com',
    url='ssh://git@endtropie.mooo.com:22222/home/git/safe.git',
    packages=['safe'],
    install_requires=['gnupg']
)