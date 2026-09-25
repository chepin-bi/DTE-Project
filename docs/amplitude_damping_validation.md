# Amplitude Damping Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states subjected to amplitude damping noise.

## Setup

- Initial state: Bell state |Φ⁺⟩
- Amplitude damping on party A with damping rate γ

## Results

| Damping γ | G | Diff |
|-----------|---|------|
| 0.0 | 0.500000 | 1.11e-16 |
| 0.1 | 0.450000 | 1.67e-16 |
| 0.3 | 0.350000 | 1.11e-16 |
| 0.5 | 0.250000 | 1.11e-16 |
| 0.7 | 0.150000 | 5.55e-17 |
| 0.9 | 0.050000 | 1.60e-16 |
| 1.0 | 0.000000 | 0.00e+00 |

## Observations

1. **G decreases linearly** with damping: G(γ) = (1−γ)·0.5
2. **Complete damping at γ=1.0**: State collapses to |00⟩, G=0
3. **G=O holds exactly** at all damping levels

## Conclusion

G=O is preserved under amplitude damping. The equality holds for both
entangled (γ<1.0) and separable (γ=1.0) states.

## Combined Noise Results

| Noise Type | G Behavior | Threshold |
|-----------|-----------|-----------|
| Depolarizing | Linear decrease | p=0.75 |
| Amplitude damping | Linear decrease | γ=1.0 |

Both confirm G=O robustness under quantum noise.
