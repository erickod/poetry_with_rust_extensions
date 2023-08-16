#!/usr/bin/env python
from threading import local
from setuptools import dist
import os

from setuptools import setup
from setuptools_rust import Binding, RustExtension


def build(setup_kwargs):
    setup(
        name="fiborusty",
        version="0.1",
        rust_extensions=[
            RustExtension(
                ".fiborusty.fiborusty",
                path="Cargo.toml",
                binding=Binding.PyO3,
            )
        ],
        packages=["fiborusty"],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
        ],
        zip_safe=False,
    )
