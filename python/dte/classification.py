"""
DTE Classification System
=========================

Advanced entanglement classification with confidence scoring and uncertainty quantification.
"""

import numpy as np
from typing import Tuple, Optional, Dict, Any, List
from dataclasses import dataclass
import logging

from .core import DTECoreEngine, DTETriple, EntanglementType

logger = logging.getLogger("dte.classification")


@dataclass
class ClassificationResult:
    """Rich classification result with metadata."""
    entanglement_type: EntanglementType
    confidence: float
    triple: DTETriple
    dims: Tuple[int, int]
    warnings: List[str]
    metadata: Dict[str, Any]


class EntanglementClassifier:
    """
    Advanced DTE classifier with confidence scoring.
    """
    
    def __init__(self, dim_a: int, dim_b: int, tol: float = 1e-10):
        self.engine = DTECoreEngine(dim_a, dim_b, tol=tol)
        self.tol = tol
        self.dims = (dim_a, dim_b)
    
    def classify(self, rho: np.ndarray) -> ClassificationResult:
        """
        Classify state with confidence scoring.
        
        Returns:
            ClassificationResult with type, confidence, warnings
        """
        warnings_list = []
        
        try:
            triple = self.engine.triple(rho)
        except Exception as e:
            logger.error(f"Computation failed: {e}")
            return ClassificationResult(
                entanglement_type=EntanglementType.UNKNOWN,
                confidence=0.0,
                triple=DTETriple(0.0, 0.0, 0.0),
                dims=self.dims,
                warnings=[str(e)],
                metadata={"error": str(e)}
            )
        
        # Check Theorem 1 consistency as quality indicator
        g_o_diff = abs(triple.G - triple.O)
        if g_o_diff > self.tol * 10:
            warnings_list.append(f"Theorem 1 violation: |G-O|={g_o_diff:.2e}")
        
        # Classification
        etype = triple.classify(tol=self.tol, dims=self.dims)
        
        # Confidence scoring
        confidence = self._compute_confidence(triple, etype, g_o_diff)
        
        # Near-boundary warnings
        if etype == EntanglementType.SEPARABLE:
            if triple.G > self.tol * 0.1:
                warnings_list.append(f"Near separable boundary: G={triple.G:.2e}")
        
        metadata = {
            "G_O_diff": g_o_diff,
            "I_over_G2": triple.I_over_G2 if triple.G > self.tol else None,
        }
        
        return ClassificationResult(
            entanglement_type=etype,
            confidence=confidence,
            triple=triple,
            dims=self.dims,
            warnings=warnings_list,
            metadata=metadata
        )
    
    def _compute_confidence(self, triple: DTETriple, etype: EntanglementType,
                            g_o_diff: float) -> float:
        """Compute classification confidence [0, 1]."""
        # Base confidence from numerical stability
        stability = max(0.0, 1.0 - g_o_diff / self.tol / 100)
        
        # Distance from boundaries
        if etype == EntanglementType.SEPARABLE:
            boundary_dist = min(triple.G, triple.I) / max(self.tol, 1e-15)
            return min(1.0, stability * (1.0 + np.log10(boundary_dist + 1) / 10))
        elif etype == EntanglementType.PPT_BOUND:
            return stability * 0.9  # PPT-bound is harder to confirm
        else:  # NPT
            return min(1.0, stability * (1.0 + triple.G / 0.1))
    
    def batch_classify(self, states: List[np.ndarray]) -> List[ClassificationResult]:
        """Classify multiple states."""
        return [self.classify(rho) for rho in states]
    
    def classify_report(self, rho: np.ndarray) -> str:
        """Generate human-readable classification report."""
        result = self.classify(rho)
        lines = [
            "=" * 60,
            "DTE Classification Report",
            "=" * 60,
            f"Dimensions: {result.dims[0]} x {result.dims[1]}",
            f"Type: {result.entanglement_type.value}",
            f"Confidence: {result.confidence:.2%}",
            "-" * 60,
            f"G (Geometric)  = {result.triple.G:.8f}",
            f"I (Information)= {result.triple.I:.8f}",
            f"O (Open)       = {result.triple.O:.8f}",
            f"DTE Score      = {result.triple.DTE_score:.8f}",
            "-" * 60,
        ]
        if result.warnings:
            lines.append("Warnings:")
            for w in result.warnings:
                lines.append(f"  - {w}")
        lines.append("=" * 60)
        return "\n".join(lines)
