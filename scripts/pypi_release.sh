#!/bin/bash
# DTE Framework PyPI Release Script
# Usage: ./scripts/pypi_release.sh

set -e

echo "DTE Framework PyPI Release v3.2.0"
echo "=================================="

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "python3 required"; exit 1; }
command -v twine >/dev/null 2>&1 || { echo "twine required: pip install twine"; exit 1; }

# Clean build artifacts
rm -rf build/ dist/ *.egg-info/

# Build package
echo "[1/4] Building package..."
cd "$(dirname "$0")/.."
python3 -m build

# Check package
echo "[2/4] Checking package..."
twine check dist/*

# Test upload (optional)
# echo "[3/4] Uploading to TestPyPI..."
# twine upload --repository testpypi dist/*

# Production upload
echo "[3/4] Uploading to PyPI..."
twine upload dist/*

echo "[4/4] Release complete!"
echo "Verify at: https://pypi.org/project/dte-core/"
