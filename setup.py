#!/usr/bin/env python
from setuptools import find_packages, setup
from conabio import src

setup(
    name="conabio",
    packages=find_packages(),
    install_requires=[
        "python-dotenv"
    ],
    version=src.version,
    description="",
    author="Conabio"
)
