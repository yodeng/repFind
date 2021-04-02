#!/usr/bin/env python
from __future__ import print_function  
from setuptools import setup

setup(
    name = "repFind",
    version = "1.0.1",
    packages = ['repFind'],
    author="Yong Deng",
    author_email = "yodeng@tju.edu.com",
    python_requires='>=2.7.10, <3',
    description = "For finding the tendom repeats in both ends of you sequence.",
    long_description = "For finding the tendom repeats in both ends of you sequence.",
    license="MIT",
    entry_points = {
        'console_scripts': [  
            'repfind = repFind.repFind:main'
        ]
    }

)
