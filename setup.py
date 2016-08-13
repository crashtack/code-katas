# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="Sum of the Nth terms",
    description="Code Wars code-kata, sum of the nth terms",
    version=0.1,
    author="David Banks",
    author_email="crashtack@gmail.com",
    license='MIT',
    py_modules=['sum_of_nth_terms'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
