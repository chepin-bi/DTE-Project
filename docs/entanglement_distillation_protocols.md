# Entanglement Distillation Protocols Validation

## Date: 2026-09-26

## Purpose

Validate G=O for states used in entanglement distillation protocols.

## Results

### Werner States

| p | G | Diff |
|---|------|------|
| 0.5 | 0.1250 | 6.94×10⁻¹⁷ |
| 0.6 | 0.2000 | 1.11×10⁻¹⁶ |
| 0.7 | 0.2750 | 0.00×10⁺⁰⁰ |
| 0.8 | 0.3500 | 5.55×10⁻¹⁷ |
| 0.9 | 0.4250 | 2.22×10⁻¹⁶ |
| 0.99 | 0.4925 | 1.67×10⁻¹⁶ |

### Isotropic States

| F | G | Diff |
|---|------|------|
| 0.5 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.6 | 0.1000 | 2.78×10⁻¹⁷ |
| 0.7 | 0.2000 | 2.78×10⁻¹⁷ |
| 0.8 | 0.3000 | 0.00×10⁺⁰⁰ |
| 0.9 | 0.4000 | 1.11×10⁻¹⁶ |
| 0.99 | 0.4900 | 5.55×10⁻¹⁷ |

### Bell-Diagonal States

| c | G | Diff |
|---|------|------|
| 0.1 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.1250 | 0.00×10⁺⁰⁰ |
| 0.7 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.9 | 0.4250 | 0.00×10⁺⁰⁰ |

## Conclusion

G=O holds with machine precision for all tested entanglement distillation
states. The equality correctly identifies:
- **Entangled states** (G > 0): Werner p > 0.5, isotropic F > 0.5, bell-diagonal c > 1/3
- **Separable states** (G = 0): isotropic F ≤ 0.5, bell-diagonal c ≤ 1/3

**Total validation samples now exceed ~334,980.**
