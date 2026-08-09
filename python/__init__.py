"""
DTE-SIUπ-AX: Derived Triangle Equivalence Unified Framework
===========================================================

A computable, strict, and complete implementation of the DTE framework
for quantum entanglement analysis, holography, neuroscience, and beyond.

Version: 3.0.0
"""

__version__ = "3.0.0"
__author__ = "SAG-ISU-UHODP-DTE Research Group"
__email__ = "chepin@163.com"

from .dte import (
    DTECoreEngine,
    DTETriple,
    StateGenerator,
    EntanglementClassifier,
    DTEConfig,
)

__all__ = [
    "DTECoreEngine",
    "DTETriple",
    "StateGenerator",
    "EntanglementClassifier",
    "DTEConfig",
]
