"""
DTE Core Engine
==============

Computes the triple invariant (G, I, O) for bipartite quantum systems.
"""

import numpy as np
from typing import Tuple, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
import logging

from .exceptions import DTEDimensionError, DTEStateError, DTENotPositiveSemidefiniteError

logger = logging.getLogger("dte.core")


class EntanglementType(Enum):
    """DTE entanglement classification."""
    SEPARABLE = "SEPARABLE"
    PPT_BOUND = "PPT-BOUND ENTANGLED"
    NPT = "NPT ENTANGLED"
    UNKNOWN = "UNKNOWN"
    
    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class DTETriple:
    """
    Immutable DTE triple invariant (G, I, O).
    
    Attributes:
        G: Geometric face = Ext^1 = Negativity
        I: Information face = Mutual Information
        O: Open face = Boundary Obstruction
    """
    G: float
    I: float
    O: float
    
    @property
    def DTE_score(self) -> float:
        """Composite DTE measure (G * I * O)."""
        if self.G > 1e-10 and self.I > 1e-10 and self.O > 1e-10:
            return self.G * self.I * self.O
        return 0.0
    
    @property
    def G_eq_O(self) -> bool:
        """Verify Theorem 1: G = O (within numerical tolerance)."""
        return abs(self.G - self.O) < 1e-9
    
    @property
    def I_over_G2(self) -> float:
        """Information-geometric ratio I / G^2."""
        if self.G > 1e-10:
            return self.I / (self.G ** 2)
        return float('inf')
    
    def classify(self, tol: float = 1e-10, dims: Optional[Tuple[int, int]] = None) -> EntanglementType:
        """
        Classify state by DTE triple.
        
        Args:
            tol: Numerical tolerance
            dims: (da, db) dimensions. Uses Horodecki theorem for 2x2/2x3.
        """
        if dims is not None and min(dims) == 2 and max(dims) <= 3:
            return EntanglementType.SEPARABLE if self.G < tol else EntanglementType.NPT
        
        if self.G < tol and self.I < tol:
            return EntanglementType.SEPARABLE
        elif self.G < tol and self.I >= tol:
            return EntanglementType.PPT_BOUND
        elif self.G >= tol and self.I >= tol:
            return EntanglementType.NPT
        return EntanglementType.UNKNOWN
    
    def to_dict(self, include_derived: bool = True) -> Dict[str, Any]:
        """Serialize to dictionary."""
        result = {"G": self.G, "I": self.I, "O": self.O}
        if include_derived:
            result.update({
                "DTE_score": self.DTE_score,
                "I_over_G2": self.I_over_G2,
                "G_eq_O": self.G_eq_O,
                "classification": self.classify().value,
            })
        return result
    
    @classmethod
    def from_dict(cls, d: Dict[str, float]) -> "DTETriple":
        """Deserialize from dictionary."""
        return cls(G=d["G"], I=d["I"], O=d["O"])
    
    def __repr__(self) -> str:
        return f"DTETriple(G={self.G:.6f}, I={self.I:.6f}, O={self.O:.6f})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DTETriple):
            return NotImplemented
        return np.isclose([self.G, self.I, self.O], [other.G, other.I, other.O]).all()
    
    def __hash__(self) -> int:
        return hash((round(self.G, 12), round(self.I, 12), round(self.O, 12)))


class DTECoreEngine:
    """
    DTE Core Engine.
    
    Computes the triple invariant (G, I, O) for bipartite quantum systems.
    """
    
    def __init__(self, dim_a: int, dim_b: int, tol: float = 1e-10, validate: bool = True):
        if dim_a < 2 or dim_b < 2:
            raise DTEDimensionError(f"Dimensions must be >= 2, got ({dim_a}, {dim_b})")
        self.da = dim_a
        self.db = dim_b
        self.d = dim_a * dim_b
        self.tol = tol
        self.validate = validate
        logger.debug(f"Initialized DTECoreEngine({dim_a}, {dim_b})")
    
    def _validate_state(self, rho: np.ndarray) -> None:
        """Validate density matrix properties."""
        if not isinstance(rho, np.ndarray):
            raise DTEStateError(f"Expected numpy array, got {type(rho)}")
        if rho.shape != (self.d, self.d):
            raise DTEStateError(f"Expected shape ({self.d}, {self.d}), got {rho.shape}")
        if not np.allclose(rho, rho.conj().T, atol=self.tol):
            raise DTEStateError("Density matrix must be Hermitian")
        
        evals = np.linalg.eigvalsh(rho)
        if np.any(evals < -self.tol):
            raise DTENotPositiveSemidefiniteError(
                f"Density matrix has negative eigenvalues: min={np.min(evals)}"
            )
        trace = np.trace(rho).real
        if abs(trace - 1.0) > self.tol:
            raise DTEStateError(f"Trace must be 1, got {trace}")
    
    def _partial_transpose(self, rho: np.ndarray) -> np.ndarray:
        """Partial transpose over subsystem A."""
        rho_tensor = rho.reshape(self.da, self.db, self.da, self.db)
        return rho_tensor.transpose(2, 1, 0, 3).reshape(self.d, self.d)
    
    def _vn_entropy(self, rho: np.ndarray) -> float:
        """von Neumann entropy S(rho) = -Tr(rho log rho)."""
        evals = np.linalg.eigvalsh(rho)
        evals = evals[evals > self.tol]
        if len(evals) == 0:
            return 0.0
        return float(-np.sum(evals * np.log2(evals)))
    
    def G(self, rho: np.ndarray) -> float:
        """Geometric face: Ext^1(rho) = Negativity(rho)."""
        if self.validate:
            self._validate_state(rho)
        rho_pt = self._partial_transpose(rho)
        evals = np.linalg.eigvalsh(rho_pt)
        trace_norm = float(np.sum(np.abs(evals)))
        return max(0.0, (trace_norm - 1.0) / 2.0)
    
    def I(self, rho: np.ndarray) -> float:
        """Information face: Mutual Information I(A:B)."""
        if self.validate:
            self._validate_state(rho)
        rho_tensor = rho.reshape(self.da, self.db, self.da, self.db)
        rho_a = np.trace(rho_tensor, axis1=1, axis2=3)
        rho_b = np.trace(rho_tensor, axis1=0, axis2=2)
        return self._vn_entropy(rho_a) + self._vn_entropy(rho_b) - self._vn_entropy(rho)
    
    def O(self, rho: np.ndarray) -> float:
        """Open face: Boundary Obstruction."""
        if self.validate:
            self._validate_state(rho)
        rho_pt = self._partial_transpose(rho)
        evals = np.linalg.eigvalsh(rho_pt)
        return float(np.sum(np.abs(evals[evals < -self.tol])))
    
    def triple(self, rho: np.ndarray) -> DTETriple:
        """Compute complete DTE triple."""
        return DTETriple(
            G=self.G(rho),
            I=self.I(rho),
            O=self.O(rho)
        )
    
    def info_geometric_constant(self, rho: np.ndarray) -> float:
        """Compute I/G^2 ratio (information-geometric constant)."""
        t = self.triple(rho)
        if t.G > self.tol:
            return t.I / (t.G ** 2)
        return float('inf')
    
    def theorem1_verify(self, rho: np.ndarray) -> Tuple[bool, float]:
        """Verify Theorem 1: G = O."""
        g = self.G(rho)
        o = self.O(rho)
        diff = abs(g - o)
        passed = diff < self.tol
        logger.debug(f"Theorem 1 verify: |G-O|={diff:.2e}, passed={passed}")
        return passed, diff
    
    def theorem2_verify(self, rho: np.ndarray) -> Tuple[bool, float]:
        """Verify Theorem 2: I >= c(d) * G^2."""
        t = self.triple(rho)
        d = min(self.da, self.db)
        c_d = 8.0 * np.log2(d) / ((d - 1) ** 2) if d > 1 else 8.0
        
        if t.G > self.tol:
            ratio = t.I / (t.G ** 2)
            passed = ratio >= c_d - self.tol
            logger.debug(f"Theorem 2 verify: I/G^2={ratio:.4f}, c(d)={c_d:.4f}, passed={passed}")
            return passed, ratio
        return True, float('inf')
    
    def batch_compute(self, states: list[np.ndarray]) -> list[DTETriple]:
        """Compute DTE triples for multiple states."""
        return [self.triple(rho) for rho in states]
    
    def __repr__(self) -> str:
        return f"DTECoreEngine(da={self.da}, db={self.db}, tol={self.tol})"
