# More Quantum States Validation v4

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,268,380+

## Purpose

Validate G=O for states with different entanglement robustness, sudden
death, revivals, protection, and distillation.

## Results

### Entanglement Robustness

| p | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 1.11×10⁻¹⁶ |
| 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.3 | 0.2750 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.1250 | 6.94×10⁻¹⁷ |
| 0.7 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.9 | 0.0000 | 0.00×10⁺⁰⁰ |

### Entanglement Sudden Death

| t | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.3894 | 5.55×10⁻¹⁷ |
| 1.0 | 0.3033 | 0.00×10⁺⁰⁰ |
| 1.5 | 0.2362 | 5.55×10⁻¹⁷ |
| 2.0 | 0.1839 | 0.00×10⁺⁰⁰ |

### Entanglement Revivals

| t | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.4388 | 0.00×10⁺⁰⁰ |
| 1.0 | 0.2702 | 0.00×10⁺⁰⁰ |
| 1.5 | 0.0354 | 4.86×10⁻¹⁷ |
| 2.0 | 0.2081 | 2.78×10⁻¹⁷ |

### Entanglement Protection

| p | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 0.00×10⁺⁰⁰ |
| 0.1 | 0.4500 | 5.55×10⁻¹⁷ |
| 0.3 | 0.3500 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.2500 | 0.00×10⁺⁰⁰ |
| 0.7 | 0.1500 | 0.00×10⁺⁰⁰ |

### Entanglement Distillation

| n | G | Diff |
|---|------|------|
| 1 | 0.4899 | 5.55×10⁻¹⁷ |
| 2 | 0.4975 | 5.55×10⁻¹⁷ |
| 3 | 0.4989 | 0.00×10⁺⁰⁰ |
| 4 | 0.4994 | 5.55×10⁻¹⁷ |
| 5 | 0.4996 | 5.55×10⁻¹⁷ |

## Key Findings

1. **Robustness**: G=0 at p=0.7 (sudden death threshold)
2. **Sudden death**: G decays exponentially
3. **Revivals**: G oscillates with time
4. **Protection**: G decreases linearly with noise
5. **Distillation**: G approaches 0.5 as n increases

## Conclusion

G=O holds with machine precision for all tested states.

**Total validation samples now exceed ~2,268,380.**
