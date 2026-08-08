"""
DTE-Core: Derived Triangle Equivalence Unified Framework
==========================================================

A computable, strict, and complete implementation of the DTE framework
for quantum entanglement analysis.

Version: 2.0.0
"""

__version__ = "2.0.0"
__author__ = "SAG-ISU-UHODP-DTE Research Group"
__email__ = "chepin@163.com"

from .dte_core import (
    DTECoreEngine,
    DTETriple,
    StateGenerator,
    DTEBenchmark,
    EntanglementType,
)

__all__ = [
    "DTECoreEngine",
    "DTETriple",
    "StateGenerator",
    "DTEBenchmark",
    "EntanglementType",
]
