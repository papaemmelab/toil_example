# toil_example

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]
[![docker badge][docker_badge]][docker_base]
[![docker badge][automated_badge]][docker_base]

A Command Line Interface created with [cookiecutter-toil](https://github.com/leukgen/cookiecutter-toil).

## Usage

This package uses docker to manage its dependencies, there are 2 ways of using it:

1. Running the [container][docker_base] in single machine mode without [`--batchSystem`] support:

        # using docker
        docker run -it leukgen/toil_example --help

        # using singularity
        singularity run docker://leukgen/toil_example --help

1. Installing the python package from [pypi][pypi_base] and passing the container as a flag:

        # install package
        pip install toil_example

        # run with docker
        toil_example [TOIL-OPTIONS] [PIPELINE-OPTIONS]
            --docker leukgen/toil_example
            --volumes <local path> <container path>
            --batchSystem LSF

        # run with singularity
        toil_example [TOIL-OPTIONS] [PIPELINE-OPTIONS]
            --singularity docker://leukgen/toil_example
            --volumes <local path> <container path>
            --batchSystem LSF
See [docker2singularity] if you want to use a [singularity] image instead of using the `docker://` prefix.

## Contributing

Contributions are welcome, and they are greatly appreciated, check our [contributing guidelines](.github/CONTRIBUTING.md)!

## Credits

This package was created using [Cookiecutter] and the
[leukgen/cookiecutter-toil] project template.

<!-- References -->
[singularity]: http://singularity.lbl.gov/
[docker2singularity]: https://github.com/singularityware/docker2singularity
[cookiecutter]: https://github.com/audreyr/cookiecutter
[leukgen/cookiecutter-toil]: https://github.com/leukgen/cookiecutter-toil
[`--batchSystem`]: http://toil.readthedocs.io/en/latest/developingWorkflows/batchSystem.html?highlight=BatchSystem

<!-- Badges -->
[docker_base]: https://hub.docker.com/r/leukgen/toil_example
[docker_badge]: https://img.shields.io/docker/build/leukgen/toil_example.svg
[automated_badge]: https://img.shields.io/docker/automated/leukgen/toil_example.svg
[codecov_badge]: https://codecov.io/gh/leukgen/toil_example/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/leukgen/toil_example
[pypi_badge]: https://img.shields.io/pypi/v/toil_example.svg
[pypi_base]: https://pypi.python.org/pypi/toil_example
[travis_badge]: https://img.shields.io/travis/leukgen/toil_example.svg
[travis_base]: https://travis-ci.org/leukgen/toil_example
