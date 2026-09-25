# Numerical Stability Test

## Date: 2026-09-25

## Purpose

Test G=O stability under numerical perturbations and noise.

## Setup

Start with Bell state |Φ⁺⟩, add random noise of magnitude ε, then
renormalize to trace=1.

## Results

### Hermitian Perturbations

| ε | G | Diff |
|---|-----|------|
| 10⁻¹⁰ | 0.500000 | 1.11e-16 |
| 10⁻⁸ | 0.500000 | 1.11e-16 |
| 10⁻⁶ | 0.500000 | 1.11e-16 |
| 10⁻⁴ | 0.499859 | 5.55e-17 |

### Non-Hermitian Perturbations (Forced Hermitian)

| ε | G | Diff |
|---|-----|------|
| 10⁻¹⁰ | 0.500000 | 1.11e-16 |
| 10⁻⁸ | 0.500000 | 0.00e+00 |
| 10⁻⁶ | 0.500001 | 2.22e-16 |

## Conclusion

G=O is numerically stable under perturbations up to ε = 10⁻⁴. The equality
holds with machine precision even when the density matrix is perturbed by
random noise.

This confirms the **robustness** of the G=O relationship for numerical
computations.
