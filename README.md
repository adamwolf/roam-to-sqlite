# roam-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/roam-to-sqlite.svg)](https://pypi.org/project/roam-to-sqlite/)
[![Changelog](https://img.shields.io/github/v/release/adamwwolf/roam-to-sqlite?include_prereleases&label=changelog)](https://github.com/adamwwolf/roam-to-sqlite/releases)
[![Tests](https://github.com/adamwwolf/roam-to-sqlite/workflows/Test/badge.svg)](https://github.com/adamwwolf/roam-to-sqlite/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/adamwwolf/roam-to-sqlite/blob/master/LICENSE)

Create an SQLite database containing your Roam Research data

## Installation

Install this tool using `pip`:

    $ pip install roam-to-sqlite

## Usage

Usage instructions go here.

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd roam-to-sqlite
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
