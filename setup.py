"""toil_example setup.py."""

from os.path import join
from os.path import abspath
from os.path import dirname

from setuptools import find_packages
from setuptools import setup

ROOT = abspath(dirname(__file__))

# see 4 > https://packaging.python.org/guides/single-sourcing-package-version/
with open(join(ROOT, "toil_example", "VERSION"), "r") as f:
    VERSION = f.read().strip()

setup(
    # single source package version
    version=VERSION,
    # in combination with recursive-includes in MANIFEST.in, non-python files
    # within the toil_example will be copied into the
    # site-packages and wheels installation directories
    include_package_data=True,
    # return a list all Python packages found within the ROOT directory
    packages=find_packages(),
    # package-specific parameters
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "toil_example=toil_example.cli:main"
        ]
    },
    setup_requires=["pytest-runner>=5.3.1"],
    install_requires=["toil_container>=2.0.0"],
    extras_require={
        "test": [
            "coverage>=5.5.0",
            "pydocstyle>=6.1.1",
            "pytest-cov>=2.12.1",
            "pytest>=6.2.5",
            "pytest-env>=0.6.2",
            "pytest-sugar>=0.9.1",
            "pylint>=1.8.1",
            "requests>=2.18.4",
            "tox>=2.9.1",
        ]
    },
    author="Juan S. Medina, Juan E. Arango",
    keywords=[],
    license="BSD",
    name="toil_example",
    test_suite="tests",
    description="A Command Line Interface created with [cookiecutter-toil](https://github.com/papaemmelab/cookiecutter-toil).",
    long_description=(
        "📘 learn more of this project on [GitHub]"
        "(https://github.com/papaemmelab/toil_example)!"
    ),
    long_description_content_type="text/markdown",
    url="https://github.com/papaemmelab/toil_example",
)
