"""
DTE-Core: Derived Triangle Equivalence Core Engine
=====================================================

A computable, strict, and complete implementation of the DTE-SIUπ-AX
framework for quantum entanglement analysis.

Version: 2.0
Date: 2026-04-20
"""

import numpy as np
from typing import Tuple, Dict, Union, Optional, List
from dataclasses import dataclass
from enum import Enum
import warnings

warnings.filterwarnings('ignore')


class EntanglementType(Enum):
    """DTE entanglement classification."""
    SEPARABLE = "SEPARABLE"                # (G=0, I=0, O=0)
    PPT_BOUND = "PPT-BOUND ENTANGLED"    # (G=0, I>0, O=0), d>=3 only
    NPT = "NPT ENTANGLED"                  # (G>0, I>0, O>0)
    UNKNOWN = "UNKNOWN"


@dataclass
class DTETriple:
    """DTE triple invariant (G, I, O)."""
    G: float  # Geometric face = Ext^1 = Negativity
    I: float  # Information face = Mutual Information
    O: float  # Open face = Boundary Obstruction
    
    @property
    def DTE_score(self) -> float:
        """Composite DTE measure."""
        if self.G > 1e-10 and self.I > 1e-10 and self.O > 1e-10:
            return self.G * self.I * self.O
        return 0.0
    
    @property
    def G_eq_O(self) -> bool:
        """Verify Theorem 1: G = O."""
        return abs(self.G - self.O) < 1e-9
    
    @property
    def I_over_G2(self) -> float:
        """Information-geometric ratio I/G^2."""
        if self.G > 1e-10:
            return self.I / (self.G ** 2)
        return float('inf')
    
    def classify(self, tol: float = 1e-10, dims: Optional[Tuple[int, int]] = None) -> EntanglementType:
        """
        Classify state by DTE triple.
        
        Args:
            tol: Numerical tolerance
            dims: (da, db) dimensions. If provided, uses low-dim theorem for 2x2/2x3.
        """
        # Low-dimensional systems: G=0 <-> separable (Horodecki theorem)
        if dims is not None and min(dims) == 2 and max(dims) <= 3:
            if self.G < tol:
                return EntanglementType.SEPARABLE
            else:
                return EntanglementType.NPT
        
        # General classification
        if self.G < tol and self.I < tol:
            return EntanglementType.SEPARABLE
        elif self.G < tol and self.I >= tol:
            return EntanglementType.PPT_BOUND
        elif self.G >= tol and self.I >= tol:
            return EntanglementType.NPT
        return EntanglementType.UNKNOWN
    
    def to_dict(self) -> Dict[str, float]:
        return {
            'G': self.G,
            'I': self.I,
            'O': self.O,
            'DTE_score': self.DTE_score,
            'I_over_G2': self.I_over_G2,
            'classification': self.classify().value
        }
    
    def __repr__(self):
        return f"DTETriple(G={self.G:.6f}, I={self.I:.6f}, O={self.O:.6f})"


class DTECoreEngine:
    """
    DTE Core Engine.
    
    Computes the triple invariant (G, I, O) for bipartite quantum systems.
    
    Theorems implemented:
    - Theorem 1: G(rho) = O(rho) exactly (all dimensions)
    - Theorem 2: I(rho) >= c(d) * G(rho)^2 (pure states)
    - Theorem 3: G=I=O=0 <-> separable (2x2, 2x3)
    - Theorem 4: PPT-bound entangled exists (d>=3)
    """
    
    def __init__(self, dim_a: int, dim_b: int, tol: float = 1e-10):
        assert dim_a >= 2 and dim_b >= 2, "Dimensions must be >= 2"
        self.da = dim_a
        self.db = dim_b
        self.d = dim_a * dim_b
        self.tol = tol
    
    def _partial_transpose(self, rho: np.ndarray) -> np.ndarray:
        """Partial transpose over subsystem A."""
        rho_tensor = rho.reshape(self.da, self.db, self.da, self.db)
        rho_pt = rho_tensor.transpose(2, 1, 0, 3).reshape(self.d, self.d)
        return rho_pt
    
    def _vn_entropy(self, rho: np.ndarray) -> float:
        """von Neumann entropy S(rho) = -Tr(rho log rho)."""
        evals = np.linalg.eigvalsh(rho)
        evals = evals[evals > self.tol]
        if len(evals) == 0:
            return 0.0
        return -np.sum(evals * np.log2(evals))
    
    def G(self, rho: np.ndarray) -> float:
        """
        Geometric face: Ext^1(rho) = Negativity(rho).
        
        Theorem 1: G(rho) = O(rho) exactly.
        
        Formula: G = max(0, (||rho^T_A||_1 - 1) / 2)
        """
        rho_pt = self._partial_transpose(rho)
        evals = np.linalg.eigvalsh(rho_pt)
        trace_norm = np.sum(np.abs(evals))
        return max(0.0, (trace_norm - 1.0) / 2.0)
    
    def I(self, rho: np.ndarray) -> float:
        """
        Information face: Mutual Information I(A:B).
        
        Formula: I = S(rho_A) + S(rho_B) - S(rho)
        """
        rho_tensor = rho.reshape(self.da, self.db, self.da, self.db)
        rho_a = np.trace(rho_tensor, axis1=1, axis2=3)
        rho_b = np.trace(rho_tensor, axis1=0, axis2=2)
        return self._vn_entropy(rho_a) + self._vn_entropy(rho_b) - self._vn_entropy(rho)
    
    def O(self, rho: np.ndarray) -> float:
        """
        Open face: Boundary Obstruction.
        
        Theorem 1: O(rho) = G(rho) exactly.
        
        Formula: O = sum_{lambda < 0} |lambda| (negative eigenvalues)
        """
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
        """
        Compute I/G^2 ratio (information-geometric constant).
        
        For dxd maximally entangled states:
            I/G^2 = 8*log2(d) / (d-1)^2
        """
        t = self.triple(rho)
        if t.G > self.tol:
            return t.I / (t.G ** 2)
        return float('inf')
    
    def theorem1_verify(self, rho: np.ndarray) -> Tuple[bool, float]:
        """Verify Theorem 1: G = O."""
        g = self.G(rho)
        o = self.O(rho)
        diff = abs(g - o)
        return diff < self.tol, diff
    
    def theorem2_verify(self, rho: np.ndarray) -> Tuple[bool, float]:
        """
        Verify Theorem 2: I >= c(d) * G^2.
        
        c(d) = 8*log2(d) / (d-1)^2 for maximally entangled states.
        """
        t = self.triple(rho)
        d = min(self.da, self.db)
        c_d = 8.0 * np.log2(d) / ((d - 1) ** 2) if d > 1 else 8.0
        
        if t.G > self.tol:
            ratio = t.I / (t.G ** 2)
            return ratio >= c_d - self.tol, ratio
        return True, float('inf')


class StateGenerator:
    """Generate standard quantum states for testing and verification."""
    
    @staticmethod
    def bell_state() -> np.ndarray:
        """Bell state |Phi+> = (|00> + |11>)/sqrt(2)."""
        psi = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def separable_state(da: int = 2, db: int = 2) -> np.ndarray:
        """Product state |0,0><0,0|."""
        rho = np.zeros((da * db, da * db), dtype=complex)
        rho[0, 0] = 1.0
        return rho
    
    @staticmethod
    def werner_state(p: float, d: int = 2) -> np.ndarray:
        """
        Werner state: rho(p) = p|Phi+><Phi+| + (1-p)I/d^2.
        
        Args:
            p: Entanglement parameter [0, 1]
            d: Dimension
        """
        phi_plus = np.zeros((d * d, d * d), dtype=complex)
        for i in range(d):
            for j in range(d):
                phi_plus[i * d + i, j * d + j] = 1.0 / d
        
        identity = np.eye(d * d) / (d * d)
        return p * phi_plus + (1.0 - p) * identity
    
    @staticmethod
    def random_pure_state(d: int, seed: Optional[int] = None) -> np.ndarray:
        """Random pure state in d-dimensional Hilbert space."""
        if seed is not None:
            np.random.seed(seed)
        psi = np.random.randn(d) + 1j * np.random.randn(d)
        psi = psi / np.linalg.norm(psi)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def random_mixed_state(d: int, rank: Optional[int] = None, 
                           seed: Optional[int] = None) -> np.ndarray:
        """Random mixed state via random density matrix."""
        if seed is not None:
            np.random.seed(seed)
        if rank is None:
            rank = d
        A = np.random.randn(d, rank) + 1j * np.random.randn(d, rank)
        rho = A @ A.conj().T
        return rho / np.trace(rho)
    
    @staticmethod
    def maximally_entangled(d: int = 2) -> np.ndarray:
        """Maximally entangled state |Phi+> = (1/sqrt(d)) sum_i |i,i>."""
        psi = np.zeros(d * d, dtype=complex)
        for i in range(d):
            psi[i * d + i] = 1.0 / np.sqrt(d)
        return np.outer(psi, psi.conj())


class DTEBenchmark:
    """Benchmark DTE engine on standard test suites."""
    
    @staticmethod
    def run_standard_tests() -> Dict[str, any]:
        """Run standard verification tests."""
        results = {}
        gen = StateGenerator()
        
        # Test 1: Bell state (2x2)
        engine_22 = DTECoreEngine(2, 2)
        bell = gen.bell_state()
        t_bell = engine_22.triple(bell)
        
        results['bell_22'] = {
            'triple': t_bell.to_dict(),
            'theorem1': engine_22.theorem1_verify(bell),
            'theorem2': engine_22.theorem2_verify(bell),
            'expected_G': 0.5,
            'expected_I': 2.0,
            'expected_O': 0.5
        }
        
        # Test 2: Separable state
        sep = gen.separable_state()
        t_sep = engine_22.triple(sep)
        results['separable_22'] = {
            'triple': t_sep.to_dict(),
            'theorem1': engine_22.theorem1_verify(sep),
            'expected_all_zero': t_sep.G < 1e-10 and t_sep.I < 1e-10 and t_sep.O < 1e-10
        }
        
        # Test 3: Werner states (2x2)
        for p in [0.0, 0.3, 0.6, 1.0]:
            werner = gen.werner_state(p, 2)
            t_w = engine_22.triple(werner)
            results[f'werner_p{p}_22'] = {
                'triple': t_w.to_dict(),
                'theorem1': engine_22.theorem1_verify(werner)
            }
        
        # Test 4: 3x3 systems
        engine_33 = DTECoreEngine(3, 3)
        max_ent_33 = gen.maximally_entangled(3)
        t_33 = engine_33.triple(max_ent_33)
        
        results['max_entangled_33'] = {
            'triple': t_33.to_dict(),
            'theorem1': engine_33.theorem1_verify(max_ent_33),
            'expected_G': 1.0,
            'I_over_G2': t_33.I_over_G2,
            'theoretical_c_d': 8.0 * np.log2(3) / 4.0
        }
        
        return results
    
    @staticmethod
    def print_report(results: Dict):
        """Print formatted benchmark report."""
        print("=" * 70)
        print("DTE-Core Benchmark Report")
        print("=" * 70)
        
        for name, data in results.items():
            print(f"\n[{name}]")
            if 'triple' in data:
                t = data['triple']
                print(f"  G = {t['G']:.6f} | I = {t['I']:.6f} | O = {t['O']:.6f}")
                print(f"  Classification: {t['classification']}")
            if 'theorem1' in data:
                passed, diff = data['theorem1']
                status = "PASS" if passed else "FAIL"
                print(f"  Theorem 1 (G=O): {status} (diff = {diff:.2e})")
            if 'theorem2' in data:
                passed, ratio = data['theorem2']
                status = "PASS" if passed else "FAIL"
                print(f"  Theorem 2 (I>=cG^2): {status} (ratio = {ratio:.4f})")
            if 'expected_all_zero' in data:
                status = "PASS" if data['expected_all_zero'] else "FAIL"
                print(f"  Separable check: {status}")
        
        print("\n" + "=" * 70)


if __name__ == "__main__":
    # Run benchmark
    results = DTEBenchmark.run_standard_tests()
    DTEBenchmark.print_report(results)
