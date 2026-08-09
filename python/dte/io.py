"""
DTE I/O Module
==============

Import/export quantum states in various formats (Qiskit, QuTiP, JSON, YAML, CSV).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, Union
import numpy as np
import logging

from .core import DTETriple
from .exceptions import DTEExportError, DTEImportError

logger = logging.getLogger("dte.io")


class StateExporter:
    """Export quantum states and DTE results to various formats."""
    
    @staticmethod
    def to_numpy(rho: np.ndarray, path: Union[str, Path]) -> None:
        """Save density matrix as .npy file."""
        np.save(Path(path), rho)
    
    @staticmethod
    def to_json(rho: np.ndarray, path: Union[str, Path], 
                triple: Optional[DTETriple] = None,
                metadata: Optional[Dict[str, Any]] = None) -> None:
        """Save state and DTE results as JSON."""
        data = {
            "density_matrix_real": rho.real.tolist(),
            "density_matrix_imag": rho.imag.tolist(),
            "shape": list(rho.shape),
        }
        if triple is not None:
            data["dte"] = triple.to_dict()
        if metadata is not None:
            data["metadata"] = metadata
        
        with open(Path(path), "w") as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def to_yaml(rho: np.ndarray, path: Union[str, Path],
                triple: Optional[DTETriple] = None,
                metadata: Optional[Dict[str, Any]] = None) -> None:
        """Save state and DTE results as YAML."""
        try:
            import yaml
            data = {
                "shape": list(rho.shape),
                "density_matrix_real": rho.real.tolist(),
                "density_matrix_imag": rho.imag.tolist(),
            }
            if triple is not None:
                data["dte"] = triple.to_dict()
            if metadata is not None:
                data["metadata"] = metadata
            
            with open(Path(path), "w") as f:
                yaml.dump(data, f, default_flow_style=False)
        except ImportError:
            raise DTEExportError("PyYAML required. Install with: pip install pyyaml")
    
    @staticmethod
    def to_qiskit(rho: np.ndarray) -> Any:
        """Convert to Qiskit DensityMatrix object."""
        try:
            from qiskit.quantum_info import DensityMatrix
            return DensityMatrix(rho)
        except ImportError:
            raise DTEExportError("Qiskit required. Install with: pip install qiskit")
    
    @staticmethod
    def to_qutip(rho: np.ndarray) -> Any:
        """Convert to QuTiP Qobj."""
        try:
            import qutip
            return qutip.Qobj(rho)
        except ImportError:
            raise DTEExportError("QuTiP required. Install with: pip install qutip")


class StateImporter:
    """Import quantum states from various formats."""
    
    @staticmethod
    def from_numpy(path: Union[str, Path]) -> np.ndarray:
        """Load density matrix from .npy file."""
        return np.load(Path(path))
    
    @staticmethod
    def from_json(path: Union[str, Path]) -> Dict[str, Any]:
        """Load state from JSON file."""
        with open(Path(path)) as f:
            data = json.load(f)
        
        real = np.array(data["density_matrix_real"])
        imag = np.array(data["density_matrix_imag"])
        rho = real + 1j * imag
        
        result = {"rho": rho}
        if "dte" in data:
            result["triple"] = DTETriple.from_dict(data["dte"])
        if "metadata" in data:
            result["metadata"] = data["metadata"]
        return result
    
    @staticmethod
    def from_qiskit(dm: Any) -> np.ndarray:
        """Convert from Qiskit DensityMatrix."""
        try:
            return np.array(dm.data)
        except AttributeError:
            raise DTEImportError("Invalid Qiskit DensityMatrix object")
    
    @staticmethod
    def from_qutip(qobj: Any) -> np.ndarray:
        """Convert from QuTiP Qobj."""
        try:
            return qobj.full()
        except AttributeError:
            raise DTEImportError("Invalid QuTiP Qobj")
