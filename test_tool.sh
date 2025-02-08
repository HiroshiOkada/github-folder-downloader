#!/bin/bash
set -e

# Create a temporary directory for testing
TMP_DIR=$(mktemp -d)
echo "Using temporary directory: ${TMP_DIR}"

echo "Installing tool in editable mode..."
pip install -e . --break-system-packages

echo "Cloning repository using git clone..."
git clone git@github.com:githubtraining/hellogitworld.git "${TMP_DIR}/hellogitworld"

echo "Using the CLI tool to download repository contents for subfolder 'src' on branch 'master'..."
github-folder-downloader https://github.com/githubtraining/hellogitworld/tree/master/src "${TMP_DIR}/hellogitworld_download"

echo "Comparing downloaded 'src' folder with the cloned repository 'src' folder..."
# Use diff to compare the contents recursively.
diff -r "${TMP_DIR}/hellogitworld/src" "${TMP_DIR}/hellogitworld_download/src"

echo "Test successful. Cleaning up temporary files..."
rm -rf "${TMP_DIR}"