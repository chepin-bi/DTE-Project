# Noise Strength Validation

## Date: 2026-09-25

## Purpose

Test G=O under depolarizing noise with different strengths.

## Setup

Apply depolarizing noise: ρ = (1-p)|Φ⁺⟩⟨Φ⁺| + p·I/4

## Results

| p | G | Diff |
|---|------|------|
| 0.01 | 0.4925 | 1.67e-16 |
| 0.05 | 0.4625 | 1.67e-16 |
| 0.10 | 0.4250 | 5.55e-17 |
| 0.20 | 0.3500 | 5.55e-17 |
| 0.30 | 0.2750 | 0.00e+00 |
| 0.50 | 0.1250 | 6.94e-17 |
| 0.70 | 0.0000 | 0.00e+00 |
| 0.90 | 0.0000 | 0.00e+00 |

## Observations

1. **G decreases with noise strength**
   - Stronger noise → less entanglement

2. **G=0 for p ≥ 0.7**
   - State becomes separable (PPT)

3. **G=O holds for all noise strengths**

## Conclusion

G=O tracks entanglement degradation correctly under depolarizing noise.
The equality identifies the separability threshold at p ≈ 0.67.
