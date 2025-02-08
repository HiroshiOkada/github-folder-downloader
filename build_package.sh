#!/bin/bash
set -e

if [ -d venv ]; then
  echo "Existing venv directory found. Removing..."
  rm -rf venv
fi

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing build module..."
pip install build

echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info*

echo "Building the package..."
python -m build

echo "Deactivating virtual environment..."
deactivate

echo "Package build complete."