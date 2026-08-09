"""
DTE Exception Hierarchy
=======================

Structured exceptions for the DTE framework.
"""


class DTEError(Exception):
    """Base exception for all DTE errors."""
    pass


class DTEDimensionError(DTEError):
    """Raised when invalid dimensions are provided."""
    pass


class DTEStateError(DTEError):
    """Raised when an invalid quantum state is provided."""
    pass


class DTENotPositiveSemidefiniteError(DTEStateError):
    """Raised when a density matrix is not positive semidefinite."""
    pass


class DTENotNormalizedError(DTEStateError):
    """Raised when a density matrix does not have trace 1."""
    pass


class DTEComputationError(DTEError):
    """Raised when a computation fails."""
    pass


class DTEExportError(DTEError):
    """Raised when exporting data fails."""
    pass


class DTEImportError(DTEError):
    """Raised when importing data fails."""
    pass


class DTEConfigurationError(DTEError):
    """Raised when configuration is invalid."""
    pass
