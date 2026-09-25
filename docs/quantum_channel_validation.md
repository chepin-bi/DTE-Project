# Quantum Channel Validation

## Date: 2026-09-25

## Purpose

Test G=O for states under different quantum channels.

## Results

| Channel | G | Diff |
|---------|---|------|
| Identity | 0.5000 | 1.11e-16 |
| Depolarizing | 0.4250 | 5.55e-17 |
| Amplitude damping | 0.4500 | 1.67e-16 |
| Phase damping | 0.4743 | 2.22e-16 |

## Conclusion

G=O holds for all tested quantum channels. The equality correctly tracks
entanglement degradation under different noise processes.
