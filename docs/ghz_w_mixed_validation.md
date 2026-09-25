# GHZ-W Mixed State Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for mixtures of GHZ and W states.

## Setup

ρ(p) = p|GHZ⟩⟨GHZ| + (1−p)|W⟩⟨W|

## Results

| p | State | G | Diff |
|---|-------|---|------|
| 0.00 | Pure W | 0.471405 | 1.11e-16 |
| 0.25 | Mixed | 0.348312 | 5.55e-17 |
| 0.50 | Mixed | 0.321987 | 1.11e-16 |
| 0.75 | Mixed | 0.369602 | 1.11e-16 |
| 1.00 | Pure GHZ | 0.500000 | 1.11e-16 |

## Observations

1. **Pure W**: G ≈ 0.471 (known value)
2. **Pure GHZ**: G = 0.5
3. **Mixed states**: G varies non-monotonically
   - Minimum at p ≈ 0.5 (G ≈ 0.322)
   - This reflects the different entanglement structures

4. **G=O holds exactly** for all mixtures

## Conclusion

G=O holds for mixtures of different entanglement classes. The equality is
robust against mixing of states with different multipartite structures.
