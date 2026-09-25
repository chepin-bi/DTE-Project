# Boundary Case Validation

## Date: 2026-09-25

## Purpose

Test G=O for states near critical boundaries (separability threshold,
maximal entanglement).

## 1. Nearly Separable States

| ε | G | Diff |
|---|-----|------|
| 10⁻¹ | 9.90×10⁻² | 5.55e-17 |
| 10⁻² | 9.99×10⁻³ | 1.04e-16 |
| 10⁻³ | 9.99×10⁻⁴ | 2.84e-17 |
| 10⁻⁴ | 1.00×10⁻⁴ | 1.11e-17 |
| 10⁻⁵ | 1.00×10⁻⁵ | 4.47e-17 |
| 10⁻⁶ | 1.00×10⁻⁶ | 8.13e-17 |

**Observation:** G=O holds exactly even for ε = 10⁻⁶.

## 2. Nearly Maximally Entangled States

| ε | G | Diff |
|---|-----|------|
| 10⁻¹ | 0.497738 | 5.55e-17 |
| 10⁻² | 0.499975 | 1.11e-16 |
| 10⁻³ | 0.500000 | 0.00e+00 |
| 10⁻⁴ | 0.500000 | 0.00e+00 |

**Observation:** G=O holds exactly for all perturbations.

## 3. Near Separability Threshold (Werner States)

| p | G | Diff |
|---|-----|------|
| 0.7400 | 0.305000 | 0.00e+00 |
| 0.7450 | 0.308750 | 1.11e-16 |
| 0.7490 | 0.311750 | 1.11e-16 |
| 0.7499 | 0.312425 | 0.00e+00 |

**Observation:** G=O holds exactly near the separability threshold.

## Conclusion

G=O is robust across all boundary cases. The equality holds with machine
precision even for:
- Infinitesimal entanglement (ε → 0)
- Near-maximal entanglement
- States arbitrarily close to the separability threshold

This confirms the **structural stability** of the G=O relationship.
