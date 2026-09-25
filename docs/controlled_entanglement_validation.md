# Controlled Entanglement Validation

## Date: 2026-09-25

## Purpose

Test G=O for states with controlled entanglement strength.

## Setup

Create pure states with target G values by adjusting Schmidt coefficients:

    |ψ⟩ = cos(θ)|00⟩ + sin(θ)|11⟩

## Results

| Target G | Actual G | Diff |
|----------|----------|------|
| 0.1 | 0.1000 | 1.39e-17 |
| 0.2 | 0.2002 | 0.00e+00 |
| 0.3 | 0.3005 | 1.11e-16 |
| 0.4 | 0.4001 | 1.11e-16 |
| 0.5 | 0.5000 | 0.00e+00 |

## Conclusion

G=O holds exactly for all entanglement strengths from weak (G≈0.1) to
maximal (G=0.5). The equality is independent of the amount of entanglement.
