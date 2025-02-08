# GitHub Folder Downloader

A CLI tool to download folders from GitHub repositories without using ZIP archives.

## Features

- Parses a GitHub repository URL.
- Recursively downloads folders and files.
- Directly creates the local directory structure.

## Installation

For development, install in editable mode:
```
pip install -e .
```

## Usage

```bash
github-folder-downloader <repo_url> <output_dir> [--branch <branch>]
```

## Development

- Use a virtual environment (venv) for development.
- Develop features on topic branches and merge into main when complete.
- Use GitHub CLI (`gh`) to create the repository and push changes.