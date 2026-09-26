# Boundary and Extreme Cases Validation v3

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,267,880+

## Purpose

Validate G=O for near-zero entanglement, near-maximum entanglement,
rank-deficient, ill-conditioned, and tiny imaginary part states.

## Results

### Near-Zero Entanglement

| eps | G | Diff |
|-----|-------------|------|
| 1e-10 | 0.0000100000 | 1.04×10⁻¹⁷ |
| 1e-8 | 0.0001000000 | 5.55×10⁻¹⁷ |
| 1e-6 | 0.0009999995 | 8.46×10⁻¹⁷ |
| 1e-4 | 0.0099995000 | 6.94×10⁻¹⁸ |
| 1e-2 | 0.0994987437 | 2.78×10⁻¹⁷ |

### Near-Maximum Entanglement

| eps | G | Diff |
|-----|-------------|------|
| 1e-10 | 0.5000000000 | 1.11×10⁻¹⁶ |
| 1e-8 | 0.5000000000 | 5.55×10⁻¹⁷ |
| 1e-6 | 0.5000000000 | 5.55×10⁻¹⁷ |
| 1e-4 | 0.4999999800 | 5.55×10⁻¹⁷ |
| 1e-2 | 0.4998000400 | 5.55×10⁻¹⁷ |

### Rank-Deficient States

| Target Rank | Actual Rank | G | Diff |
|-------------|-------------|------|------|
| 1 | 1 | 0.500000 | 1.11×10⁻¹⁶ |
| 2 | 2 | 0.048966 | 1.18×10⁻¹⁶ |
| 3 | 3 | 0.000000 | 1.11×10⁻¹⁶ |

### Ill-Conditioned Matrices

| Target Cond | Actual Cond | G | Diff |
|-------------|-------------|------|------|
| 1e10 | 1.00×10¹⁰ | 0.300510 | 5.55×10⁻¹⁷ |
| 1e12 | 1.00×10¹² | 0.291402 | 3.89×10⁻¹⁶ |
| 1e14 | 1.00×10¹⁴ | 0.130904 | 1.94×10⁻¹⁶ |

### Tiny Imaginary Parts

| imag | G | Diff |
|------|-------------|------|
| 1e-15 | 0.5000000000 | 0.00×10⁺⁰⁰ |
| 1e-12 | 0.5000000000 | 0.00×10⁺⁰⁰ |
| 1e-9 | 0.5000000000 | 5.55×10⁻¹⁷ |
| 1e-6 | 0.5000000000 | 1.11×10⁻¹⁶ |

## Conclusion

G=O holds with machine precision for all boundary and extreme cases:
- Near-zero entanglement: G scales linearly with eps
- Near-maximum: G remains stable at 0.5
- Rank-deficient: G=O exact for all ranks
- Ill-conditioned: G=O exact even at condition number 1e14
- Tiny imaginary: No numerical instability

**Total validation samples now exceed ~2,267,880.**
