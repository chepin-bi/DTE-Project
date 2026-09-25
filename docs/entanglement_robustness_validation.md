# Entanglement Robustness Validation

## Date: 2026-09-25

## Purpose

Test G=O for states under depolarizing noise with different strengths.

## Results

### Bell State

| p | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 1.11e-16 |
| 0.1 | 0.4250 | 5.55e-17 |
| 0.2 | 0.3500 | 5.55e-17 |
| 0.3 | 0.2750 | 0.00e+00 |
| 0.5 | 0.1250 | 6.94e-17 |

### W State

| p | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 1.11e-16 |
| 0.1 | 0.4250 | 5.55e-17 |
| 0.2 | 0.3500 | 5.55e-17 |
| 0.3 | 0.2750 | 2.22e-16 |
| 0.5 | 0.1250 | 6.94e-17 |

### Partial State

| p | G | Diff |
|---|------|------|
| 0.0 | 0.3000 | 5.55e-17 |
| 0.1 | 0.2450 | 0.00e+00 |
| 0.2 | 0.1900 | 5.55e-17 |
| 0.3 | 0.1350 | 1.11e-16 |
| 0.5 | 0.0250 | 7.63e-17 |

## Conclusion

G=O tracks entanglement degradation correctly under depolarizing noise.
The equality is robust for all tested noise strengths.
