#!/bin/bash
set -e

if [ -d test_env ]; then
  echo "Existing test_env directory found. Removing..."
  rm -rf test_env
fi

echo "Creating a fresh virtual environment for testing installation..."
python3 -m venv test_env
source test_env/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

# Find the latest wheel package in dist/
WHEEL_PACKAGE=$(ls -t dist/*.whl | head -n 1)
if [ -z "$WHEEL_PACKAGE" ]; then
  echo "No wheel package found in dist/"
  exit 1
fi

echo "Installing wheel package: $WHEEL_PACKAGE"
pip install "$WHEEL_PACKAGE"

echo "Running package test..."
# Running help to test installation without requiring positional arguments.
github-folder-downloader --help

echo "Test completed successfully. Deactivating test environment..."
deactivate