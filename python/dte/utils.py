"""
DTE Utility Functions
=====================

Helper utilities for state validation, conversions, and mathematical operations.
"""

import numpy as np
from typing import Tuple
import logging

logger = logging.getLogger("dte.utils")


def is_hermitian(rho: np.ndarray, tol: float = 1e-10) -> bool:
    """Check if matrix is Hermitian."""
    return np.allclose(rho, rho.conj().T, atol=tol)


def is_positive_semidefinite(rho: np.ndarray, tol: float = 1e-10) -> bool:
    """Check if matrix is positive semidefinite."""
    evals = np.linalg.eigvalsh(rho)
    return np.all(evals >= -tol)


def is_density_matrix(rho: np.ndarray, tol: float = 1e-10) -> Tuple[bool, str]:
    """
    Comprehensive density matrix validation.
    
    Returns:
        (is_valid, error_message)
    """
    if rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        return False, f"Must be square matrix, got shape {rho.shape}"
    
    if not is_hermitian(rho, tol):
        diff = np.max(np.abs(rho - rho.conj().T))
        return False, f"Not Hermitian (max diff={diff:.2e})"
    
    if not is_positive_semidefinite(rho, tol):
        evals = np.linalg.eigvalsh(rho)
        return False, f"Not positive semidefinite (min eig={np.min(evals):.2e})"
    
    trace = np.trace(rho).real
    if abs(trace - 1.0) > tol:
        return False, f"Trace={trace:.6f} != 1"
    
    return True, "Valid density matrix"


def partial_trace_a(rho: np.ndarray, da: int, db: int) -> np.ndarray:
    """Partial trace over subsystem A."""
    rho_tensor = rho.reshape(da, db, da, db)
    return np.trace(rho_tensor, axis1=0, axis2=2)


def partial_trace_b(rho: np.ndarray, da: int, db: int) -> np.ndarray:
    """Partial trace over subsystem B."""
    rho_tensor = rho.reshape(da, db, da, db)
    return np.trace(rho_tensor, axis1=1, axis2=3)


def schmidt_decomposition(psi: np.ndarray, da: int, db: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Schmidt decomposition of a pure bipartite state.
    
    Returns:
        (U, S, Vh) where psi = sum_k S_k |u_k> |v_k>
    """
    matrix = psi.reshape(da, db)
    U, S, Vh = np.linalg.svd(matrix, full_matrices=False)
    return U, S, Vh


def concurrence(rho: np.ndarray) -> float:
    """
    Wootters concurrence for 2-qubit states.
    
    Only valid for 4x4 density matrices.
    """
    if rho.shape != (4, 4):
        raise ValueError("Concurrence only defined for 2-qubit (4x4) states")
    
    sigma_y = np.array([[0, -1j], [1j, 0]])
    R = np.kron(sigma_y, sigma_y) @ rho.conj() @ np.kron(sigma_y, sigma_y)
    
    # Eigenvalues of rho @ R
    evals = np.linalg.eigvals(rho @ R)
    evals = np.sort(np.abs(evals))[::-1]
    
    return max(0, np.sqrt(evals[0]) - np.sqrt(evals[1]) - np.sqrt(evals[2]) - np.sqrt(evals[3]))


def fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
    """Quantum fidelity F(rho, sigma) = Tr(sqrt(sqrt(rho) sigma sqrt(rho)))^2."""
    from scipy.linalg import sqrtm
    sqrt_rho = sqrtm(rho)
    return float(np.real(np.trace(sqrtm(sqrt_rho @ sigma @ sqrt_rho)) ** 2))
