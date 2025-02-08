from setuptools import setup, find_packages

setup(
    name="github-folder-downloader",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "github-folder-downloader=github_folder_downloader.cli:main",
        ],
    },
    install_requires=[
        "requests"
    ],
    description="A CLI tool to download folders from GitHub repositories.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/github-folder-downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)