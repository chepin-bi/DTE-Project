#!/usr/bin/env python3
"""
DTE + Holography Demo
=====================

Demonstrates DTE-Holographic Principle coupling.

This is a conceptual demo showing how DTE triples could map
to holographic quantities. Full AdS/CFT implementation requires
numerical GR and is beyond scope.
"""

import numpy as np
import sys
sys.path.insert(0, '../python')

from dte_core import DTECoreEngine, StateGenerator

def thermofield_double_state(beta, E_n, n_max=10):
    """
    Construct thermofield double state.
    
    |TFD> = sum_n exp(-beta*E_n/2) |n>_L |n>_R / Z
    
    Simplified: use equally spaced energy levels.
    """
    energies = np.array([E_n * i for i in range(n_max)])
    coeffs = np.exp(-beta * energies / 2)
    coeffs = coeffs / np.linalg.norm(coeffs)
    
    # Construct density matrix in product basis
    d = n_max
    psi = np.zeros(d * d, dtype=complex)
    for i in range(n_max):
        psi[i * d + i] = coeffs[i]
    
    return np.outer(psi, psi.conj())

def rt_area_proxy(beta, d=2):
    """
    Proxy for Ryu-Takayanagi area.
    
    For BTZ black hole: Area ~ c/3 * log(beta)
    Simplified scaling.
    """
    return np.log(max(beta, 0.1)) * d / 3.0

print("=" * 70)
print("DTE + Holography Coupling Demo")
print("=" * 70)

# Thermofield double states at different temperatures
print("\n[Thermofield Double States]")
print("-" * 50)

for beta in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    rho = thermofield_double_state(beta, E_n=1.0, n_max=4)
    engine = DTECoreEngine(4, 4)
    t = engine.triple(rho)
    area = rt_area_proxy(beta, d=4)
    
    # DTE-HP conjecture: G ∝ Area
    print(f"  β={beta:5.2f}: G={t.G:.4f} | I={t.I:.4f} | O={t.O:.4f} | Area_proxy={area:.4f}")

print("\n[Scaling Analysis]")
print("-" * 50)

betas = np.logspace(-1, 1, 20)
Gs = []
areas = []

for beta in betas:
    rho = thermofield_double_state(beta, E_n=1.0, n_max=4)
    engine = DTECoreEngine(4, 4)
    Gs.append(engine.G(rho))
    areas.append(rt_area_proxy(beta, d=4))

# Correlation
corr = np.corrcoef(Gs, areas)[0, 1]
print(f"  Correlation(G, Area_proxy) = {corr:.4f}")
print(f"  {'Strong correlation!' if corr > 0.8 else 'Weak correlation'}")

print("\n" + "=" * 70)
