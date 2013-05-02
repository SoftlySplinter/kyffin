#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name             = 'kyffin',
    version          = '0.1',
    url              = 'kyffin.alexanderdbrown.com',

    maintainer       = 'Alexander D Brown',
    maintainer_email = 'alex@alexanderdbrown.com',

    description      = 'Kyffin Williams: Digital Analysis of Paintings',
    long_description = open('README.rst').read(),

    classifiers      = [
        'Development Status :: 2 - Pre-Alpha',
    ],

    # Package
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts':['kyffin = kyffin:run']
    },

    # Requirements
    install_requires=[
        'flask'
    ],
)
