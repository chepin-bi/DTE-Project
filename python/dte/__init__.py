"""
DTE-SIUπ-AX: Derived Triangle Equivalence Unified Framework
==============================================================

A computable, strict, and complete implementation of the DTE framework
for quantum entanglement analysis, holography, neuroscience, and beyond.

Quick Start:
    >>> from dte import DTECoreEngine, StateGenerator
    >>> engine = DTECoreEngine(2, 2)
    >>> rho = StateGenerator.bell_state()
    >>> triple = engine.triple(rho)
    >>> print(triple)
    DTETriple(G=0.500000, I=2.000000, O=0.500000)

Modules:
    core        - DTE triple computation engine
    states      - Quantum state generators
    classification - Entanglement type classification
    io          - Import/export (Qiskit, QuTiP, JSON, YAML)
    viz         - Visualization (3D fingerprint, evolution plots)
    cli         - Command-line interface
    config      - Configuration management
    api         - RESTful Web API (FastAPI)

Version: 3.0.0
"""

__version__ = "3.0.0"
__author__ = "SAG-ISU-UHODP-DTE Research Group"
__email__ = "chepin@163.com"
__license__ = "MIT"
__url__ = "https://github.com/chepin-ai/DTE-Project"

from .core import DTECoreEngine, DTETriple, EntanglementType
from .states import StateGenerator
from .classification import EntanglementClassifier
from .config import DTEConfig
from .exceptions import DTEDimensionError, DTEStateError, DTENotPositiveSemidefiniteError
from .attestation import AttestationAnalyzer, AttestationFace, AttestationStatus

__all__ = [
    "DTECoreEngine",
    "DTETriple",
    "EntanglementType",
    "StateGenerator",
    "EntanglementClassifier",
    "DTEConfig",
    "DTEDimensionError",
    "DTEStateError",
    "DTENotPositiveSemidefiniteError",
    "AttestationAnalyzer",
    "AttestationFace",
    "AttestationStatus",
    "__version__",
]
