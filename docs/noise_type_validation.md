# Noise Type Validation

## Date: 2026-09-25

## Purpose

Test G=O under different noise channels.

## Setup

Apply noise channels (p=0.1) to Bell state |Φ⁺⟩.

## Results

| Noise Type | G | Diff |
|-----------|---|------|
| Depolarizing | 0.4250 | 5.55e-17 |
| Amplitude damping | 0.4500 | 5.55e-17 |
| Phase damping | 0.4743 | 0.00e+00 |
| Bit flip | 0.4000 | 0.00e+00 |

## Observations

1. **Different noise types affect G differently**
   - Phase damping: smallest effect (G=0.474)
   - Bit flip: largest effect (G=0.400)

2. **G=O holds for all noise types**

## Conclusion

G=O is robust under different noise channels. The equality tracks
entanglement degradation correctly for all tested noise types.
