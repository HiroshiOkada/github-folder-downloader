# GitHub Folder Downloader

GitHub Folder Downloader is a command line tool to download folders from GitHub repositories without zipping. It supports specifying branch and subpath.

## Features

- Download folders from GitHub repositories.
- Specify branch and subpath.
- Command line interface for ease of use.

## Installation

You can install the package from PyPI using pip:

    pip install github-folder-downloader

## Usage

Basic usage:

    github-folder-downloader <repo_url> <output_dir>

Optional arguments:

    --branch BRANCH     The branch to download from (default: main)
    --subpath SUBPATH   The repository sub-path to download (default: root)

For more information, use:

    github-folder-downloader --help

## Maintainer

- PyPi Username: toycode
- Full Name: Hiroshi Okada
- Public Email: okadahiroshi@miobox.jp

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.