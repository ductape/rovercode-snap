#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup
from setuptools import find_packages

package_name = 'rovercode'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['contrib','docs','tests']),
    license='License :: OSI Approved :: GPLv3 License',
    entry_points={
        'console_scripts': [
            'rovercode=rovercode.main:main',
        ],
    },
)
