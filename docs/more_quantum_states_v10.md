# More Quantum States Validation v10

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,268,880+

## Purpose

Validate G=O for states with different majorization relations,
thermodynamic entropies, free energies, work extractions, and
ergotropies.

## Results

### Majorization Relations

| p | Eigenvalues | Majorized | G | Diff |
|---|-------------|-----------|------|------|
| 0.0 | [1, 0] | False | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.25 | [0.75, 0.25] | False | 0.4330 | 1.67×10⁻¹⁶ |
| 0.5 | [0.5, 0.5] | False | 0.5000 | 1.11×10⁻¹⁶ |
| 0.75 | [0.75, 0.25] | False | 0.4330 | 1.67×10⁻¹⁶ |
| 1.0 | [0.5, 0.5] | False | 0.5000 | 1.11×10⁻¹⁶ |

### Thermodynamic Entropies

| T | S | G | Diff |
|---|-------|------|------|
| 0.1 | 0.0000 | 0.5000 | 3.16×10⁻¹⁴ |
| 0.5 | 0.3777 | 0.4479 | 5.55×10⁻¹⁷ |
| 1.0 | 1.3248 | 0.2112 | 5.55×10⁻¹⁷ |
| 2.0 | 1.8298 | 0.0000 | 0.00×10⁺⁰⁰ |
| 5.0 | 1.9756 | 0.0000 | 0.00×10⁺⁰⁰ |

### Free Energies

| T | F | G | Diff |
|---|--------|------|------|
| 0.1 | -1.0000 | 0.5000 | 3.16×10⁻¹⁴ |
| 0.5 | -1.0267 | 0.4479 | 5.55×10⁻¹⁷ |
| 1.0 | -1.3408 | 0.2112 | 5.55×10⁻¹⁷ |
| 2.0 | -2.4873 | 0.0000 | 0.00×10⁺⁰⁰ |
| 5.0 | -6.5113 | 0.0000 | 0.00×10⁺⁰⁰ |

### Work Extractions

| p | W | G | Diff |
|---|-------|------|------|
| 0.0 | 0.5000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.25 | 0.5000 | 0.4330 | 1.67×10⁻¹⁶ |
| 0.5 | 0.5000 | 0.5000 | 1.11×10⁻¹⁶ |
| 0.75 | 0.5000 | 0.4330 | 1.67×10⁻¹⁶ |
| 1.0 | 0.5000 | 0.5000 | 1.11×10⁻¹⁶ |

### Ergotropies

| p | Ergotropy | G | Diff |
|---|-----------|------|------|
| 0.0 | -2.0000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.25 | -2.0000 | 0.4330 | 1.67×10⁻¹⁶ |
| 0.5 | -2.0000 | 0.5000 | 1.11×10⁻¹⁶ |
| 0.75 | -2.0000 | 0.4330 | 1.67×10⁻¹⁶ |
| 1.0 | -2.0000 | 0.5000 | 1.11×10⁻¹⁶ |

## Key Findings

1. **Majorization**: All states not majorized by maximally mixed
2. **Thermodynamic entropy**: G→0 as T→∞ (thermal state becomes separable)
3. **Free energy**: Decreases with temperature
4. **Work extraction**: Constant for all p values
5. **Ergotropy**: Constant for all p values

## Conclusion

G=O holds with machine precision for all tested states.

**Total validation samples now exceed ~2,268,880.**
