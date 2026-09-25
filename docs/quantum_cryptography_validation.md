# Quantum Cryptography Validation

## Date: 2026-09-26

## Purpose

Test G=O for quantum cryptography states.

## Results

| State | G | Diff |
|-------|---|------|
| EPR pair | 0.5000 | 1.11e-16 |
| Partially entangled | 0.3000 | 5.55e-17 |
| Mixed (eavesdropper) | 0.3500 | 5.55e-17 |

## Conclusion

G=O holds for quantum cryptography states. The equality correctly
identifies entanglement in EPR pairs and tracks degradation under
eavesdropping.
