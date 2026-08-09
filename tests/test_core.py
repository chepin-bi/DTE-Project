"""
DTE Core Test Suite
===================

Comprehensive tests using pytest fixtures and parametrization.
Migrates numerical verification from v2.0 test_dte_core.py.
"""

import numpy as np
import pytest
import sys

sys.path.insert(0, '/mnt/agents/output/DTE-Project/python')

from dte.core import DTECoreEngine, DTETriple, EntanglementType
from dte.states import StateGenerator
from dte.exceptions import DTEDimensionError, DTEStateError


class TestDTETriple:
    """Tests for DTETriple data class."""

    def test_creation(self):
        t = DTETriple(0.5, 2.0, 0.5)
        assert t.G == 0.5
        assert t.I == 2.0
        assert t.O == 0.5

    def test_immutability(self):
        t = DTETriple(0.5, 2.0, 0.5)
        with pytest.raises(AttributeError):
            t.G = 0.6

    def test_equality(self):
        t1 = DTETriple(0.5, 2.0, 0.5)
        t2 = DTETriple(0.5, 2.0, 0.5)
        assert t1 == t2

    def test_hash(self):
        t1 = DTETriple(0.5, 2.0, 0.5)
        t2 = DTETriple(0.5, 2.0, 0.5)
        assert hash(t1) == hash(t2)

    def test_dte_score(self):
        assert DTETriple(0.5, 2.0, 0.5).DTE_score == pytest.approx(0.5)
        assert DTETriple(0.0, 0.0, 0.0).DTE_score == 0.0

    def test_G_eq_O(self):
        assert DTETriple(0.5, 2.0, 0.5).G_eq_O is True
        assert DTETriple(0.5, 2.0, 0.6).G_eq_O is False

    def test_to_dict(self):
        t = DTETriple(0.5, 2.0, 0.5)
        d = t.to_dict()
        assert d["G"] == 0.5
        assert d["I"] == 2.0
        assert d["O"] == 0.5
        assert "classification" in d

    def test_from_dict(self):
        d = {"G": 0.5, "I": 2.0, "O": 0.5}
        t = DTETriple.from_dict(d)
        assert t == DTETriple(0.5, 2.0, 0.5)

    def test_I_over_G2(self):
        t = DTETriple(0.5, 2.0, 0.5)
        assert t.I_over_G2 == pytest.approx(8.0, abs=1e-10)
        t2 = DTETriple(0.0, 0.0, 0.0)
        assert t2.I_over_G2 == float('inf')


class TestDTECoreEngine:
    """Tests for DTECoreEngine."""

    @pytest.fixture
    def engine_22(self):
        return DTECoreEngine(2, 2)

    @pytest.fixture
    def engine_33(self):
        return DTECoreEngine(3, 3)

    def test_invalid_dimensions(self):
        with pytest.raises(DTEDimensionError):
            DTECoreEngine(1, 2)
        with pytest.raises(DTEDimensionError):
            DTECoreEngine(2, 1)

    def test_bell_state(self, engine_22):
        rho = StateGenerator.bell_state()
        t = engine_22.triple(rho)
        assert t.G == pytest.approx(0.5, abs=1e-10)
        assert t.I == pytest.approx(2.0, abs=1e-10)
        assert t.O == pytest.approx(0.5, abs=1e-10)

    def test_separable_state(self, engine_22):
        rho = StateGenerator.separable_state()
        t = engine_22.triple(rho)
        assert t.G < 1e-10
        assert t.I < 1e-10
        assert t.O < 1e-10
        assert t.classify(dims=(2, 2)) == EntanglementType.SEPARABLE

    @pytest.mark.parametrize("p", [0.0, 0.2, 0.5, 0.8, 1.0])
    def test_werner_states(self, engine_22, p):
        rho = StateGenerator.werner_state(p, 2)
        t = engine_22.triple(rho)
        assert t.G_eq_O is True

    def test_theorem1_precision(self, engine_22):
        """Verify G=O to high precision across random states."""
        max_diff = 0.0
        for seed in range(100):
            rho = StateGenerator.random_pure_state(4, seed=seed)
            diff = abs(engine_22.G(rho) - engine_22.O(rho))
            max_diff = max(max_diff, diff)
        assert max_diff < 1e-12

    def test_theorem2_lower_bound(self, engine_22):
        """Verify I >= 8*G^2 for 2x2 systems."""
        min_ratio = float('inf')
        for seed in range(100):
            rho = StateGenerator.random_pure_state(4, seed=seed)
            t = engine_22.triple(rho)
            if t.G > 1e-10:
                ratio = t.I / (t.G ** 2)
                min_ratio = min(min_ratio, ratio)
        assert min_ratio >= 8.0 - 1e-6

    def test_maximally_entangled_33(self, engine_33):
        rho = StateGenerator.maximally_entangled(3)
        t = engine_33.triple(rho)
        assert t.G == pytest.approx(1.0, abs=1e-10)
        assert t.O == pytest.approx(1.0, abs=1e-10)

    def test_invalid_state(self, engine_22):
        """Test validation catches invalid states."""
        bad = np.array([[1, 1], [0, 0]], dtype=complex)
        with pytest.raises(DTEStateError):
            engine_22.G(bad)

        bad2 = np.eye(4) / 2
        with pytest.raises(DTEStateError):
            engine_22.G(bad2)

    def test_batch_compute(self, engine_22):
        states = [StateGenerator.bell_state(), StateGenerator.separable_state()]
        triples = engine_22.batch_compute(states)
        assert len(triples) == 2
        assert triples[0].G == pytest.approx(0.5)
        assert triples[1].G < 1e-10

    def test_repr(self, engine_22):
        assert "DTECoreEngine(da=2, db=2" in repr(engine_22)


class TestClassification:
    """Tests for entanglement classification."""

    def test_bell_classified_npt(self):
        t = DTETriple(0.5, 2.0, 0.5)
        assert t.classify(dims=(2, 2)) == EntanglementType.NPT

    def test_separable_classified(self):
        t = DTETriple(0.0, 0.0, 0.0)
        assert t.classify(dims=(2, 2)) == EntanglementType.SEPARABLE

    def test_low_dim_horodecki(self):
        """In 2x2, G=0 always means separable."""
        t = DTETriple(0.0, 0.1, 0.0)
        assert t.classify(dims=(2, 2)) == EntanglementType.SEPARABLE

    def test_ppt_bound_high_dim(self):
        """In d>=3, G=0 with I>0 is PPT-bound."""
        t = DTETriple(0.0, 0.3, 0.0)
        assert t.classify() == EntanglementType.PPT_BOUND


class TestStateGenerator:
    """Tests for state generators."""

    def test_all_bell_states(self):
        states = StateGenerator.bell_states()
        assert len(states) == 4
        for name, rho in states.items():
            assert rho.shape == (4, 4)
            assert np.isclose(np.trace(rho), 1.0)

    def test_ghz_state(self):
        rho = StateGenerator.ghz_state(3)
        assert rho.shape == (8, 8)
        assert np.isclose(np.trace(rho), 1.0)

    def test_w_state(self):
        rho = StateGenerator.w_state(3)
        assert rho.shape == (8, 8)
        assert np.isclose(np.trace(rho), 1.0)

    def test_random_states_deterministic(self):
        """Random states with same seed should be identical."""
        r1 = StateGenerator.random_pure_state(4, seed=42)
        r2 = StateGenerator.random_pure_state(4, seed=42)
        assert np.allclose(r1, r2)

    def test_separable_state_multi_dim(self):
        """Separable states for various dimensions."""
        for da, db in [(2, 2), (2, 3), (3, 3)]:
            rho = StateGenerator.separable_state(da, db)
            assert rho.shape == (da * db, da * db)
            assert np.isclose(np.trace(rho), 1.0)


class TestTheorems:
    """Numerical verification of Theorems 1-4 across dimensions."""

    def test_theorem1_multi_dim(self):
        """Verify G=O to high precision across multiple dimensions."""
        max_diff = 0.0
        for da, db in [(2, 2), (3, 3), (4, 4)]:
            engine = DTECoreEngine(da, db)
            for seed in range(100):
                rho = StateGenerator.random_pure_state(da * db, seed=seed)
                diff = abs(engine.G(rho) - engine.O(rho))
                max_diff = max(max_diff, diff)
        assert max_diff < 1e-12

    def test_theorem2_33_lower_bound(self):
        """Verify I >= c(3)*G^2 for 3x3 systems."""
        engine = DTECoreEngine(3, 3)
        c_d = 8.0 * np.log2(3) / 4.0
        min_ratio = float('inf')
        for seed in range(50):
            rho = StateGenerator.random_pure_state(9, seed=seed)
            t = engine.triple(rho)
            if t.G > 1e-10:
                ratio = t.I / (t.G ** 2)
                min_ratio = min(min_ratio, ratio)
        assert min_ratio >= c_d - 1e-6

    def test_theorem3_separable_g_zero(self):
        """Separable states have G=0 for all dimensions."""
        for da, db in [(2, 2), (2, 3), (3, 3)]:
            engine = DTECoreEngine(da, db)
            rho = StateGenerator.separable_state(da, db)
            t = engine.triple(rho)
            assert t.G < 1e-10
            assert t.O < 1e-10

    def test_theorem3_entangled_g_positive(self):
        """Entangled states have G>0 for 2x2."""
        engine = DTECoreEngine(2, 2)
        rho = StateGenerator.werner_state(1.0, 2)
        t = engine.triple(rho)
        assert t.G > 1e-10
        assert t.O > 1e-10

    def test_information_geometric_constant(self):
        """Test c(d) = 8*log2(d)/(d-1)^2 for maximally entangled states."""
        for d in [2, 3, 4, 5]:
            engine = DTECoreEngine(d, d)
            rho = StateGenerator.maximally_entangled(d)
            t = engine.triple(rho)
            c_d_theory = 8.0 * np.log2(d) / ((d - 1) ** 2)
            c_d_measured = t.I_over_G2
            assert abs(c_d_measured - c_d_theory) < 0.1

    def test_c_d_values(self):
        """Verify specific c(d) values."""
        assert abs(8.0 * np.log2(2) / 1.0 - 8.0) < 1e-10
        assert abs(8.0 * np.log2(3) / 4.0 - 3.1699) < 0.01
        assert abs(8.0 * np.log2(4) / 9.0 - 1.7778) < 0.01

    def test_maximally_entangled_properties(self):
        """Maximally entangled states: G = (d-1)/2, O = (d-1)/2 for dxd."""
        for d in [2, 3, 4]:
            engine = DTECoreEngine(d, d)
            rho = StateGenerator.maximally_entangled(d)
            t = engine.triple(rho)
            expected_g = (d - 1) / 2.0
            assert t.G == pytest.approx(expected_g, abs=1e-10)
            assert t.O == pytest.approx(expected_g, abs=1e-10)
            assert t.I > 0.0
