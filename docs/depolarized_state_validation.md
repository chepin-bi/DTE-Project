# Depolarized State Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states subjected to depolarizing noise.

## Setup

- Initial state: Bell state |Φ⁺⟩
- Depolarizing channel: ρ(p) = (1−p)|Φ⁺⟩⟨Φ⁺| + p·I/4

## Results

| Noise p | G | Diff |
|---------|---|------|
| 0.0 | 0.500000 | 1.11e-16 |
| 0.1 | 0.425000 | 5.55e-17 |
| 0.3 | 0.275000 | 0.00e+00 |
| 0.5 | 0.125000 | 6.94e-17 |
| 0.7 | 0.000000 | 0.00e+00 |
| 0.9 | 0.000000 | 0.00e+00 |
| 1.0 | 0.000000 | 0.00e+00 |

## Observations

1. **G decreases linearly** with noise: G(p) = (1−p)·0.5
2. **Threshold at p=0.75**: State becomes separable (G=0)
3. **G=O holds exactly** at all noise levels

## Conclusion

G=O is preserved under depolarizing noise. The equality holds for both
entangled (p<0.75) and separable (p≥0.75) states.
