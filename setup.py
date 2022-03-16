import codecs
import os.path

from setuptools import find_packages
from setuptools import setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname("__file__"))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


this_directory = os.path.abspath(os.path.dirname("__file__"))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "seaborn>=0.11.0",
    # "jupyter>=1.0.0",
]

tests_require = [
    "pytest>=6.2.0",
    "pytest-cov>=2.11.0",
    "pytest-mock>=3.5.0",
    "pytest-mpl>=0.12",
]

setup_requires: list = []

packages = find_packages()

setup(
    name="learn_sphinx_doc",
    version=get_version("learn_sphinx_doc/__init__.py"),
    description="Example package used to learn how to make sphinx documentation.",
    url="https://github.com/jameshtwose/learning_sphinx_documentation",
    author="James Twose",
    author_email="contact@jamestwose.com",
    license="BSD (3-clause)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
)
