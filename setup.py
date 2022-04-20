#!/usr/bin/env python
from setuptools import find_packages, setup
import sipecam

setup(
    name="sipecam",
    packages=find_packages(),
    install_requires=[
        "python-dotenv"
    ],
    version=sipecam.version,
    description="",
    author="Conabio"
)
