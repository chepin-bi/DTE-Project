"""
DTE-Core Test Suite v2.0
=========================

Comprehensive tests for Theorems 1-4 and DTE classification.
Run: python -m pytest tests/test_dte_core.py -v
"""

import numpy as np
import sys
sys.path.insert(0, '/mnt/agents/output/DTE-Project/python')

from dte_core import DTECoreEngine, StateGenerator, DTETriple, EntanglementType


def test_theorem1_G_eq_O():
    """Test Theorem 1: G = O exactly for all dimensions."""
    print("\n[Test] Theorem 1: G = O (exact equality)")
    print("-" * 50)
    
    gen = StateGenerator()
    test_cases = [
        ("Bell (2x2)", 2, 2, gen.bell_state()),
        ("Separable (2x2)", 2, 2, gen.separable_state()),
        ("Werner p=0.5", 2, 2, gen.werner_state(0.5, 2)),
        ("Max Entangled (3x3)", 3, 3, gen.maximally_entangled(3)),
        ("Random pure (4x4)", 4, 4, gen.random_pure_state(16, seed=42)),
    ]
    
    all_pass = True
    for name, da, db, rho in test_cases:
        engine = DTECoreEngine(da, db)
        g = engine.G(rho)
        o = engine.O(rho)
        diff = abs(g - o)
        passed = diff < 1e-9
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  {name:25s} | G={g:.6f} | O={o:.6f} | diff={diff:.2e} | {status}")
    
    print(f"\n  Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return all_pass


def test_theorem2_info_geometric():
    """Test Theorem 2: I >= c(d) * G^2."""
    print("\n[Test] Theorem 2: I >= c(d) * G^2")
    print("-" * 50)
    
    gen = StateGenerator()
    all_pass = True
    
    for da, db in [(2, 2), (3, 3)]:
        engine = DTECoreEngine(da, db)
        d = min(da, db)
        c_d = 8.0 * np.log2(d) / ((d - 1) ** 2) if d > 1 else 8.0
        
        min_ratio = float('inf')
        for seed in range(100):
            rho = gen.random_pure_state(da * db, seed=seed)
            t = engine.triple(rho)
            if t.G > 1e-10:
                ratio = t.I / (t.G ** 2)
                min_ratio = min(min_ratio, ratio)
        
        passed = min_ratio >= c_d - 1e-6
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  {da}x{db}: min(I/G^2) = {min_ratio:.4f} >= c({d}) = {c_d:.4f} | {status}")
    
    print(f"\n  Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return all_pass


def test_theorem3_low_dim_equivalence():
    """Test Theorem 3: G=0 <-> separable for 2x2, 2x3 (Horodecki)."""
    print("\n[Test] Theorem 3: Low-dimensional equivalence")
    print("-" * 50)
    
    gen = StateGenerator()
    all_pass = True
    
    # Test separable states: G should be 0
    for da, db in [(2, 2), (2, 3)]:
        engine = DTECoreEngine(da, db)
        rho = gen.separable_state(da, db)
        t = engine.triple(rho)
        
        passed = (t.G < 1e-10) and (t.O < 1e-10)
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  Separable {da}x{db}: G={t.G:.2e}, O={t.O:.2e} | {status}")
    
    # Test entangled states: G should be > 0
    for da, db in [(2, 2)]:
        engine = DTECoreEngine(da, db)
        rho = gen.werner_state(1.0, min(da, db))
        t = engine.triple(rho)
        
        passed = (t.G > 1e-10) and (t.O > 1e-10)
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  Entangled {da}x{db}: G={t.G:.4f}, O={t.O:.4f} | {status}")
    
    print(f"\n  Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return all_pass


def test_classification():
    """Test DTE classification with dimension-aware logic."""
    print("\n[Test] DTE Classification")
    print("-" * 50)
    
    gen = StateGenerator()
    engine = DTECoreEngine(2, 2)
    
    # For 2x2: G=0 -> SEPARABLE, G>0 -> NPT (Horodecki theorem)
    test_cases = [
        ("Separable", gen.separable_state(), EntanglementType.SEPARABLE),
        ("Bell", gen.bell_state(), EntanglementType.NPT),
        ("Werner p=0.2", gen.werner_state(0.2, 2), EntanglementType.SEPARABLE),
        ("Werner p=0.8", gen.werner_state(0.8, 2), EntanglementType.NPT),
    ]
    
    all_pass = True
    for name, rho, expected in test_cases:
        t = engine.triple(rho)
        cls = t.classify(dims=(2, 2))
        passed = cls == expected
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  {name:20s} | {cls.value:25s} | expected {expected.value:25s} | {status}")
    
    print(f"\n  Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return all_pass


def test_numerical_precision():
    """Test numerical precision of G = O."""
    print("\n[Test] Numerical Precision (Theorem 1)")
    print("-" * 50)
    
    gen = StateGenerator()
    max_diff = 0.0
    
    for da, db in [(2, 2), (3, 3), (4, 4)]:
        engine = DTECoreEngine(da, db)
        for seed in range(100):
            rho = gen.random_pure_state(da * db, seed=seed)
            diff = abs(engine.G(rho) - engine.O(rho))
            max_diff = max(max_diff, diff)
    
    passed = max_diff < 1e-12
    status = "PASS" if passed else "FAIL"
    print(f"  Max |G - O| over 300 states: {max_diff:.2e}")
    print(f"  Result: {status}")
    return passed


def test_information_geometric_constant():
    """Test c(d) = 8*log2(d)/(d-1)^2 for maximally entangled states."""
    print("\n[Test] Information-Geometric Constant c(d)")
    print("-" * 50)
    
    gen = StateGenerator()
    all_pass = True
    
    for d in [2, 3, 4, 5]:
        engine = DTECoreEngine(d, d)
        rho = gen.maximally_entangled(d)
        t = engine.triple(rho)
        
        c_d_theory = 8.0 * np.log2(d) / ((d - 1) ** 2)
        c_d_measured = t.I_over_G2 if t.G > 1e-10 else float('inf')
        
        # For maximally entangled states, should approximately equal
        passed = abs(c_d_measured - c_d_theory) < 0.1 if t.G > 1e-10 else False
        status = "PASS" if passed else "FAIL"
        all_pass = all_pass and passed
        print(f"  d={d}: c(d)_theory={c_d_theory:.4f} | c(d)_measured={c_d_measured:.4f} | {status}")
    
    print(f"\n  Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    return all_pass


def run_all_tests():
    """Run complete test suite."""
    print("=" * 70)
    print("DTE-Core Test Suite v2.0")
    print("=" * 70)
    
    results = {
        "Theorem 1 (G=O)": test_theorem1_G_eq_O(),
        "Theorem 2 (I>=cG^2)": test_theorem2_info_geometric(),
        "Theorem 3 (Low-dim equiv)": test_theorem3_low_dim_equivalence(),
        "Classification": test_classification(),
        "Numerical Precision": test_numerical_precision(),
        "Info-Geometric c(d)": test_information_geometric_constant(),
    }
    
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    
    total = len(results)
    passed = sum(results.values())
    
    for name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"  {name:35s} | {status}")
    
    print("\n" + "=" * 70)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 70)
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
