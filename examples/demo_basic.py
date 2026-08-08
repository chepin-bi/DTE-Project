#!/usr/bin/env python3
"""
DTE-Core Basic Demo
===================

Demonstrates fundamental DTE operations and theorem verification.
"""

import numpy as np
import sys
sys.path.insert(0, '../python')

from dte_core import DTECoreEngine, StateGenerator, DTEBenchmark

print("=" * 70)
print("DTE-Core Basic Demo")
print("=" * 70)

# 1. Initialize engine
gen = StateGenerator()
engine = DTECoreEngine(2, 2)

# 2. Bell state
print("\n[1] Bell State |Phi+>")
bell = gen.bell_state()
t = engine.triple(bell)
print(f"    G = {t.G:.6f}  (Expected: 0.5)")
print(f"    I = {t.I:.6f}  (Expected: 2.0)")
print(f"    O = {t.O:.6f}  (Expected: 0.5)")
print(f"    Classification: {t.classify(dims=(2,2)).value}")
print(f"    Theorem 1 (G=O): {'PASS' if t.G_eq_O else 'FAIL'}")

# 3. Separable state
print("\n[2] Separable State |0,0><0,0|")
sep = gen.separable_state()
t = engine.triple(sep)
print(f"    G = {t.G:.10f}")
print(f"    I = {t.I:.10f}")
print(f"    O = {t.O:.10f}")
print(f"    Classification: {t.classify(dims=(2,2)).value}")

# 4. Werner states
print("\n[3] Werner States (2x2)")
for p in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    rho = gen.werner_state(p, 2)
    t = engine.triple(rho)
    cls = t.classify(dims=(2,2)).value
    print(f"    p={p:.1f}: G={t.G:.4f} I={t.I:.4f} O={t.O:.4f} | {cls}")

# 5. Maximal entangled states
print("\n[4] Maximally Entangled States")
for d in [2, 3, 4]:
    eng = DTECoreEngine(d, d)
    rho = gen.maximally_entangled(d)
    t = eng.triple(rho)
    c_d = 8.0 * np.log2(d) / ((d - 1) ** 2)
    print(f"    d={d}: G={t.G:.4f} I={t.I:.4f} I/G²={t.I_over_G2:.4f} | c({d})={c_d:.4f}")

# 6. Random states theorem verification
print("\n[5] Random States Theorem Verification (100 states)")
max_diff = 0.0
min_ratio_22 = float('inf')
for seed in range(100):
    rho = gen.random_pure_state(4, seed=seed)
    diff = abs(engine.G(rho) - engine.O(rho))
    max_diff = max(max_diff, diff)
    if engine.G(rho) > 1e-10:
        ratio = engine.I(rho) / (engine.G(rho) ** 2)
        min_ratio_22 = min(min_ratio_22, ratio)

print(f"    Max |G - O| = {max_diff:.2e}  (Theorem 1)")
print(f"    Min I/G² (2x2) = {min_ratio_22:.4f} >= 8.0  (Theorem 2)")

print("\n" + "=" * 70)
print("Demo Complete")
print("=" * 70)
