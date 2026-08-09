"""
Pytest Configuration and Fixtures
=================================
"""

import sys
import numpy as np
import pytest

sys.path.insert(0, '/mnt/agents/output/DTE-Project/python')

from dte.core import DTECoreEngine
from dte.states import StateGenerator


@pytest.fixture(scope="session")
def state_gen():
    """Shared StateGenerator instance."""
    return StateGenerator()


@pytest.fixture(scope="session")
def engine_22():
    """2x2 DTE engine."""
    return DTECoreEngine(2, 2)


@pytest.fixture(scope="session")
def engine_33():
    """3x3 DTE engine."""
    return DTECoreEngine(3, 3)


@pytest.fixture
def bell_state(state_gen):
    """Bell state fixture."""
    return state_gen.bell_state()


@pytest.fixture
def separable_state(state_gen):
    """Separable state fixture."""
    return state_gen.separable_state()


@pytest.fixture
def random_pure_22(state_gen):
    """Random pure 2-qubit state fixture."""
    return state_gen.random_pure_state(4, seed=42)
