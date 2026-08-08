"""Setup script for DTE-Core."""

from setuptools import setup, find_packages

setup(
    name="dte-core",
    version="2.0.0",
    description="Derived Triangle Equivalence (DTE) unified framework for quantum entanglement analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SAG-ISU-UHODP-DTE Research Group",
    author_email="chepin@163.com",
    url="https://github.com/yourusername/DTE-Project",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "flake8>=4.0",
            "black>=22.0",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="quantum-entanglement information-theory category-theory lean4",
)
