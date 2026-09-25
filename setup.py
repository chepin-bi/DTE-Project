"""Setup script for DTE Framework."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dte-core",
    version="3.2.0",
    author="DTE Research Group",
    author_email="chepin@163.com",
    description="Derived Triangle Equivalence Framework for Quantum Entanglement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chepin-ai/DTE-Project",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "viz": ["matplotlib>=3.3.0", "seaborn>=0.11.0"],
        "api": ["fastapi>=0.68.0", "uvicorn>=0.15.0", "pydantic>=1.8.0"],
        "dev": ["pytest>=6.2.0", "black>=21.0", "mypy>=0.910", "flake8>=3.9.0"],
        "all": [
            "matplotlib>=3.3.0", "seaborn>=0.11.0",
            "fastapi>=0.68.0", "uvicorn>=0.15.0", "pydantic>=1.8.0",
            "pytest>=6.2.0", "black>=21.0", "mypy>=0.910", "flake8>=3.9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dte=dte.cli:main",
        ],
    },
)
