from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="roam-to-sqlite",
    description="Create an SQLite database containing your Roam Research data",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Adam Wolf",
    url="https://github.com/adamwwolf/roam-to-sqlite",
    project_urls={
        "Issues": "https://github.com/adamwwolf/roam-to-sqlite/issues",
        "CI": "https://github.com/adamwwolf/roam-to-sqlite/actions",
        "Changelog": "https://github.com/adamwwolf/roam-to-sqlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["roam_to_sqlite"],
    entry_points="""
        [console_scripts]
        roam-to-sqlite=roam_to_sqlite.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    tests_require=["roam-to-sqlite[test]"],
    python_requires=">=3.6",
)
