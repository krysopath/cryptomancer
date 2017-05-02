#!/usr/bin/env python3
# coding=utf-8
"""
Setupfile for safe

"""
from setuptools import setup

out = setup(
    name='safe',
    version='0.1',
    description='safe module, contains crypto related helpers',
    url='ssh://git@endtropie.mooo.com:22222/home/git/safe.git',
    author='Georg',
    author_email='krysopath@gmail.com',
    license='GPL',
    packages=['safe'],
    install_requires=[
        'gnupg',
    ],
    zip_safe=False
)
