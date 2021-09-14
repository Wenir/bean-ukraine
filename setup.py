import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bean_ukraine",
    version = "0.0.1",
    author = "Wenir",
    author_email = "wenir.spam@yahoo.com",
    description = ("An NBU prices fetcher"),
    license = "BSD",
    keywords = "beancount beanprice bean-price ua ukraine NBU",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['bean_ukraine'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
    ],
)

# https://pythonhosted.org/an_example_pypi_project/setuptools.html
