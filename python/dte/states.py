"""
DTE State Generators
====================

Generate standard and random quantum states for testing and analysis.
"""

import numpy as np
from typing import Optional, Tuple
import logging

from .exceptions import DTEDimensionError

logger = logging.getLogger("dte.states")


class StateGenerator:
    """Generate standard quantum states for testing and verification."""
    
    @staticmethod
    def bell_state() -> np.ndarray:
        """Bell state |Phi+> = (|00> + |11>)/sqrt(2)."""
        psi = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def bell_states() -> dict[str, np.ndarray]:
        """All four Bell states."""
        states = {}
        for name, coeffs in [
            ("Phi+", [1, 0, 0, 1]),
            ("Phi-", [1, 0, 0, -1]),
            ("Psi+", [0, 1, 1, 0]),
            ("Psi-", [0, 1, -1, 0]),
        ]:
            psi = np.array(coeffs, dtype=complex) / np.sqrt(2.0)
            states[name] = np.outer(psi, psi.conj())
        return states
    
    @staticmethod
    def separable_state(da: int = 2, db: int = 2) -> np.ndarray:
        """Product state |0,0><0,0|."""
        rho = np.zeros((da * db, da * db), dtype=complex)
        rho[0, 0] = 1.0
        return rho
    
    @staticmethod
    def product_state(psi_a: np.ndarray, psi_b: np.ndarray) -> np.ndarray:
        """Arbitrary product state |psi_a> ⊗ |psi_b>."""
        return np.kron(np.outer(psi_a, psi_a.conj()), np.outer(psi_b, psi_b.conj()))
    
    @staticmethod
    def werner_state(p: float, d: int = 2) -> np.ndarray:
        """
        Werner state: rho(p) = p|Phi+><Phi+| + (1-p)I/d^2.
        
        Args:
            p: Entanglement parameter [0, 1]
            d: Dimension
        """
        if not (0 <= p <= 1):
            raise ValueError(f"p must be in [0, 1], got {p}")
        phi_plus = np.zeros((d * d, d * d), dtype=complex)
        for i in range(d):
            for j in range(d):
                phi_plus[i * d + i, j * d + j] = 1.0 / d
        identity = np.eye(d * d) / (d * d)
        return p * phi_plus + (1.0 - p) * identity
    
    @staticmethod
    def isotropic_state(p: float, d: int = 2) -> np.ndarray:
        """
        Isotropic state: rho(p) = p|Phi+><Phi+| + (1-p)I/d^2.
        (Same formula as Werner in this convention)
        """
        return StateGenerator.werner_state(p, d)
    
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
        """Random mixed state via Ginibre ensemble."""
        if seed is not None:
            np.random.seed(seed)
        if rank is None:
            rank = d
        A = np.random.randn(d, rank) + 1j * np.random.randn(d, rank)
        rho = A @ A.conj().T
        return rho / np.trace(rho)
    
    @staticmethod
    def random_separable_state(da: int, db: int, seed: Optional[int] = None) -> np.ndarray:
        """Random separable state (product of random pure states)."""
        if seed is not None:
            np.random.seed(seed)
        psi_a = np.random.randn(da) + 1j * np.random.randn(da)
        psi_a = psi_a / np.linalg.norm(psi_a)
        psi_b = np.random.randn(db) + 1j * np.random.randn(db)
        psi_b = psi_b / np.linalg.norm(psi_b)
        return StateGenerator.product_state(psi_a, psi_b)
    
    @staticmethod
    def maximally_entangled(d: int = 2) -> np.ndarray:
        """Maximally entangled state |Phi+> = (1/sqrt(d)) sum_i |i,i>."""
        psi = np.zeros(d * d, dtype=complex)
        for i in range(d):
            psi[i * d + i] = 1.0 / np.sqrt(d)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def ghz_state(n: int = 3) -> np.ndarray:
        """GHZ state for n qubits."""
        d = 2 ** n
        psi = np.zeros(d, dtype=complex)
        psi[0] = 1.0 / np.sqrt(2.0)
        psi[d - 1] = 1.0 / np.sqrt(2.0)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def w_state(n: int = 3) -> np.ndarray:
        """W state for n qubits."""
        d = 2 ** n
        psi = np.zeros(d, dtype=complex)
        for i in range(n):
            psi[1 << i] = 1.0 / np.sqrt(n)
        return np.outer(psi, psi.conj())
    
    @staticmethod
    def graph_state(adjacency: np.ndarray) -> np.ndarray:
        """
        Graph state from adjacency matrix.
        
        Args:
            adjacency: n x n symmetric binary adjacency matrix
        """
        n = adjacency.shape[0]
        # Start with |+>^⊗n
        plus = np.array([1, 1]) / np.sqrt(2)
        state = plus
        for _ in range(n - 1):
            state = np.kron(state, plus)
        
        # Apply controlled-Z for each edge
        cz = np.eye(4)
        cz[3, 3] = -1
        
        for i in range(n):
            for j in range(i + 1, n):
                if adjacency[i, j]:
                    # Apply CZ between i and j
                    op = np.eye(2 ** n)
                    # This is simplified; full implementation needs proper gate decomposition
                    pass
        
        return np.outer(state, state.conj())
