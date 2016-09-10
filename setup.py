# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="Code Katas",
    description="Code Wars code-kata",
    version=0.1,
    author="David Banks",
    author_email="crashtack@gmail.com",
    license='MIT',
    py_modules=['sum_of_nth_terms'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
