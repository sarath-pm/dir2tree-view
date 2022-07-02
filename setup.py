import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="dir2tree-view",
    version="1.0",
    author="Sarath P M",
    author_email="sarath2375@gmail.com",
    description="Print/generate directory tree with icons",
    long_description="Module to print/generate directory tree with icons",
    long_description_content_type="text/markdown",
    url="https://github.com/sarath-pm/dir2tree-view",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)