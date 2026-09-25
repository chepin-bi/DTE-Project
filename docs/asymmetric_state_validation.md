# Asymmetric State Validation

## Date: 2026-09-25

## Purpose

Test G=O for states with asymmetric structure (unequal Schmidt coefficients,
non-uniform bipartitions, rank-deficient mixed states).

## Results

### 1. Asymmetric Pure States (2×3)

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.444819 | 0.00e+00 |
| 2 | 0.371550 | 0.00e+00 |
| 3 | 0.437348 | 2.78e-16 |
| 4 | 0.487164 | 2.78e-16 |
| 5 | 0.187262 | 2.78e-16 |

### 2. Unequal Schmidt Coefficients (2×2)

| a | G | Diff |
|---|-----|------|
| 0.90 | 0.392301 | 0.00e+00 |
| 0.80 | 0.480000 | 5.55e-17 |
| 0.70 | 0.499900 | 0.00e+00 |
| 0.60 | 0.480000 | 0.00e+00 |
| 0.55 | 0.459341 | 5.55e-17 |

### 3. Rank-2 Mixed States

| p | G | Diff |
|---|-----|------|
| 0.1 | 0.400000 | 0.00e+00 |
| 0.3 | 0.200000 | 1.11e-16 |
| 0.5 | 0.000000 | 0.00e+00 |
| 0.7 | 0.200000 | 1.94e-16 |
| 0.9 | 0.400000 | 0.00e+00 |

## Conclusion

G=O holds exactly for all asymmetric states tested. The equality is
independent of:
- Schmidt coefficient symmetry
- Bipartition uniformity
- Rank or eigenvalue distribution

**Total: 15/15 tests passed (100%)**
