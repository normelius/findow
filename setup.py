
from setuptools import setup, find_packages


NAME = "findow"
AUTHOR = "Anton Normelius"
EMAIL = "a.normelius@gmail.com"
URL = "https://github.com/normelius/findow"

PACKAGES = ['findow']

# Read readme.
with open("README.md", "r") as fh:
    long_description = fh.read()

# Read requirements.
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    version="0.01",
    packages=find_packages(),
    install_requires=required,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
