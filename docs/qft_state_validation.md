# QFT-Related State Validation

## Date: 2026-09-25

## Purpose

Test G=O for Quantum Fourier Transform (QFT) and Hadamard states.

## Results

### QFT States

| System | G | n_neg | Diff |
|--------|---|-------|------|
| 2×2 | 0.0000 | 0 | 7.93e-18 |
| 3×3 | 0.4467 | 1 | 2.78e-17 |
| 4×4 | 0.3977 | 2 | 2.22e-16 |

### Hadamard States

| System | G | n_neg | Diff |
|--------|---|-------|------|
| 2-qubit (2|2) | 0.0000 | 0 | 1.06e-16 |
| 3-qubit (4|2) | 0.0000 | 0 | 9.24e-17 |
| 4-qubit (8|2) | 0.0000 | 0 | 6.44e-17 |

## Observations

1. **Hadamard states are separable** (G=0)
   - Uniform superposition factorizes across qubits

2. **QFT states are entangled** (G>0 for d≥3)
   - 3×3 QFT has G=0.447 with 1 negative PT eigenvalue
   - 4×4 QFT has G=0.398 with 2 negative PT eigenvalues

3. **G=O holds exactly** for all QFT-related states

## Conclusion

G=O applies to quantum algorithm states including QFT and Hadamard states.
The equality distinguishes separable Hadamard states from entangled QFT
states.
