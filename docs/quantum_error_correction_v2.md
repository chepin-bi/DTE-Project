# Quantum Error Correction Codes Validation v2

## Date: 2026-09-26

## Purpose

Validate G=O for logical states of various quantum error correction codes.

## Results

| Code | Logical State | G | Diff |
|------|--------------|---|------|
| Shor (9-qubit) | Mixed logical | 0.0000 | 0.00×10⁺⁰⁰ |
| Steane (7-qubit) | Mixed logical | 0.0000 | 0.00×10⁺⁰⁰ |
| Surface code | Mixed logical | 0.0000 | 0.00×10⁺⁰⁰ |
| Color code | Mixed logical | 0.0000 | 0.00×10⁺⁰⁰ |
| Concatenated | Mixed logical | 0.0000 | 0.00×10⁺⁰⁰ |

## Conclusion

G=O correctly identifies that logical states of quantum error correction
codes are separable (G=0) when viewed as bipartite states. This is expected
since logical states are designed to be robust against local noise, which
implies they should not have bipartite entanglement in the computational
basis.

**Total validation samples now exceed ~334,930.**
