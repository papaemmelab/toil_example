# toil_example

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]

A Command Line Interface created with [cookiecutter-toil](https://github.com/leukgen/cookiecutter-toil).

# Features

* 📦 &nbsp; **Installation**

        # local
        pip install --editable .

        # pypi (if available)
        pip install toil_example

* 🍉 &nbsp; **Usage**

        toil_example --help

* 🐳 &nbsp; **Container Usage**

    Check our docker hub for toil_example images. Alternatively clone this repo and build the image yourself.

        toil_example
            --shared-fs <path to shared file system e.g. /ifs>
            --docker {or --singularity} <image path or name>
            jobstore
        

    If you need to use [singularity], check [docker2singularity], and use `-m '/shared-fs-path /shared-fs-path'` to make sure your shared file system is mounted inside the singularity image.

# Contributing

Contributions are welcome, and they are greatly appreciated, check our [contributing guidelines](CONTROBUTING.md)!

<!-- References -->
[singularity]: http://singularity.lbl.gov/
[docker2singularity]: https://github.com/singularityware/docker2singularity

<!-- Badges -->
[codecov_badge]: https://codecov.io/gh/leukgen/toil_example/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/leukgen/toil_example
[pypi_badge]: https://img.shields.io/pypi/v/toil_example.svg
[pypi_base]: https://pypi.python.org/pypi/toil_example
[travis_badge]: https://img.shields.io/travis/leukgen/toil_example.svg
[travis_base]: https://travis-ci.org/leukgen/toil_example
