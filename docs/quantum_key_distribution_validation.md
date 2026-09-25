# Quantum Key Distribution Validation

## Date: 2026-09-25

## Purpose

Test G=O for quantum key distribution states.

## Results

| State | G | Diff |
|-------|---|------|
| \|0⟩ | 0.0000 | 0.00e+00 |
| \|1⟩ | 0.0000 | 0.00e+00 |
| \|+⟩ | 0.0000 | 0.00e+00 |
| \|-⟩ | 0.0000 | 0.00e+00 |
| Bell (E91) | 0.5000 | 1.11e-16 |

## Conclusion

G=O correctly identifies that BB84 states are separable (G=0) while E91
Bell pairs are entangled (G=0.5).
