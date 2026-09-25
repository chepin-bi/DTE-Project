# Measurement Outcome Validation

## Date: 2026-09-25

## Purpose

Test G=O for post-measurement states.

## Setup

Start with Bell state |Φ⁺⟩, measure first qubit in Z or X basis.

## Results

| State | G | Diff |
|-------|---|------|
| Initial Bell | 0.5000 | 1.11e-16 |
| Z-meas (outcome 0) | 0.0000 | 0.00e+00 |
| Z-meas (outcome 1) | 0.0000 | 0.00e+00 |
| X-meas (outcome 0) | 0.0000 | 1.06e-16 |
| X-meas (outcome 1) | 0.0000 | 1.06e-16 |

## Observations

1. **Post-measurement states are separable** (G=0)
   - Measurement destroys entanglement

2. **G=O holds for all post-measurement states**

## Conclusion

G=O applies to post-measurement states. The equality correctly identifies
that projective measurements destroy entanglement.
