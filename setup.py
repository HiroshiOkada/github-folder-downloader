from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-folder-downloader",
    version="0.1.0",
    author="Hiroshi Okada",
    author_email="okadahiroshi@miobox.jp",
    maintainer="toycode",
    maintainer_email="okadahiroshi@miobox.jp",
    description="A command line tool to download folders from GitHub repositories without zipping.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HiroshiOkada/github-folder-downloader",
    project_urls={
        "PyPI": "https://pypi.org/user/toycode",
        "Source": "https://github.com/HiroshiOkada/github-folder-downloader"
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "github-folder-downloader=github_folder_downloader.cli:main"
        ]
    },
    install_requires=[
        "requests"
    ],
)