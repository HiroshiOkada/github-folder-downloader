# Publishing Instructions for GitHub Folder Downloader

This document outlines the steps to publish your package to PyPI and test it on TestPyPI.

## 1. Pre-Publish Preparations
- Ensure that you have updated the package metadata in setup.py.
- Make sure the LICENSE, README.md, and other documentation files are up-to-date.
- Verify that all tests pass using the provided test script:
  
      bash test_install_package.sh

## 2. Build the Package
- Run the build script to create distribution files:
  
      bash build_package.sh

- This script creates both a source distribution (sdist) and a wheel (.whl) file in the dist/ directory.
- The script also runs `twine check` to validate the built distributions.

## 3. Publish to PyPI
- If the package validation passes, publish the package using twine:
  
      twine upload dist/*

- When prompted, use the following credentials:
  - PyPI Username: toycode
  - Full Name: Hiroshi Okada
  - Public Email: okadahiroshi@miobox.jp

## 4. Test on TestPyPI
- Before publishing to the live PyPI, it is recommended to test your package on TestPyPI.
- Build your package using:
  
      bash build_package.sh

- Upload the package to TestPyPI with twine:
  
      twine upload --repository testpypi dist/*

- Ensure you have an account on TestPyPI.
- Install your package from TestPyPI in a fresh virtual environment:
  
      pip install --index-url https://test.pypi.org/simple/ github-folder-downloader

- Verify that the package functions as expected.

## 5. Post-Publish
- Verify that the package is published by checking your PyPI project page.
- Inform users of the new release through your project’s README or website.

## Troubleshooting
- Ensure you have installed the required packages (twine, build) in your virtual environment.
- Use `twine check dist/*` to verify package integrity before uploading.

This concludes the publishing process.