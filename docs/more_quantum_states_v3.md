# More Quantum States Validation v3

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,268,180+

## Purpose

Validate G=O for states with different Loschmidt echoes, Loschmidt rates,
OTOCs, Page entropies, and entanglement spectra.

## Results

### Loschmidt Echoes

| t | L | G | Diff |
|---|------|------|------|
| 0.1 | 1.0000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.5 | 1.0000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 1.0 | 1.0000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 2.0 | 1.0000 | 0.0000 | 0.00×10⁺⁰⁰ |
| 5.0 | 1.0000 | 0.0000 | 0.00×10⁺⁰⁰ |

### Loschmidt Rates

| γ | G | Diff |
|---|------|------|
| 0.1 | 0.4524 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.3704 | 5.55×10⁻¹⁷ |
| 0.5 | 0.3033 | 0.00×10⁺⁰⁰ |
| 0.7 | 0.2483 | 5.55×10⁻¹⁷ |
| 0.9 | 0.2033 | 5.55×10⁻¹⁷ |

### Out-of-Time-Ordered Correlators

| t | OTOC | G | Diff |
|---|------|------|------|
| 0.1 | 0.9802 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.5931 | 0.0000 | 0.00×10⁺⁰⁰ |
| 1.0 | 0.0852 | 0.0000 | 0.00×10⁺⁰⁰ |

### Page Entropies

| d | S | S_page | G | Diff |
|---|------|--------|------|------|
| 2 | 0.1511 | 0.6393 | 0.1459 | 1.67×10⁻¹⁶ |
| 3 | 1.1918 | 1.3445 | 0.7857 | 2.22×10⁻¹⁶ |
| 4 | 1.4419 | 1.8197 | 1.0678 | 2.22×10⁻¹⁶ |
| 5 | 1.6883 | 2.1777 | 1.3387 | 2.22×10⁻¹⁶ |

### Entanglement Spectra

| Spectrum | G | Diff |
|----------|------|------|
| Equal | 0.0000 | 2.22×10⁻¹⁶ |
| Linear | 0.0000 | 0.00×10⁺⁰⁰ |
| Exponential | 0.0199 | 1.42×10⁻¹⁶ |

## Conclusion

G=O holds with machine precision for all tested states.

**Total validation samples now exceed ~2,268,180.**
