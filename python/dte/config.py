"""
DTE Configuration Management
===========================

Centralized configuration for the DTE framework.
Supports YAML, JSON, environment variables, and Python dicts.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from pathlib import Path


@dataclass
class DTEConfig:
    """
    DTE framework configuration.
    
    Attributes:
        tol: Numerical tolerance for computations
        max_dim: Maximum supported Hilbert space dimension
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        cache_enabled: Whether to cache computation results
        parallel_enabled: Whether to enable parallel processing
        backend: Computational backend (numpy, torch, jax)
        auto_validate: Whether to auto-validate input states
        precision: Floating point precision (float32, float64)
    """
    tol: float = 1e-10
    max_dim: int = 1024
    log_level: str = "INFO"
    cache_enabled: bool = True
    parallel_enabled: bool = False
    backend: str = "numpy"
    auto_validate: bool = True
    precision: str = "float64"
    
    # Plugin settings
    plugins: Dict[str, Any] = field(default_factory=dict)
    
    # Visualization settings
    viz_backend: str = "matplotlib"
    viz_theme: str = "default"
    
    # API settings
    api_host: str = "127.0.0.1"
    api_port: int = 8080
    api_debug: bool = False
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "DTEConfig":
        """Create config from dictionary."""
        valid_keys = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in config_dict.items() if k in valid_keys}
        return cls(**filtered)
    
    @classmethod
    def from_env(cls, prefix: str = "DTE_") -> "DTEConfig":
        """Create config from environment variables."""
        config = cls()
        for key, value in os.environ.items():
            if key.startswith(prefix):
                attr_name = key[len(prefix):].lower()
                if hasattr(config, attr_name):
                    # Type conversion
                    current_val = getattr(config, attr_name)
                    if isinstance(current_val, bool):
                        value = value.lower() in ("true", "1", "yes")
                    elif isinstance(current_val, int):
                        value = int(value)
                    elif isinstance(current_val, float):
                        value = float(value)
                    setattr(config, attr_name, value)
        return config
    
    @classmethod
    def from_yaml(cls, path: str) -> "DTEConfig":
        """Load config from YAML file."""
        try:
            import yaml
            with open(path) as f:
                return cls.from_dict(yaml.safe_load(f))
        except ImportError:
            raise ImportError("PyYAML required for YAML config. Install with: pip install pyyaml")
    
    @classmethod
    def from_json(cls, path: str) -> "DTEConfig":
        """Load config from JSON file."""
        import json
        with open(path) as f:
            return cls.from_dict(json.load(f))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return {
            f.name: getattr(self, f.name)
            for f in self.__dataclass_fields__.values()
        }
    
    def to_yaml(self, path: str) -> None:
        """Save config to YAML file."""
        try:
            import yaml
            with open(path, "w") as f:
                yaml.dump(self.to_dict(), f, default_flow_style=False)
        except ImportError:
            raise ImportError("PyYAML required for YAML export.")
    
    def to_json(self, path: str) -> None:
        """Save config to JSON file."""
        import json
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
