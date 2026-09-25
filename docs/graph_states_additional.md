# Graph States Validation (Additional)

## Date: 2026-09-25

## Purpose

Test G=O for different graph topologies (star, line, ring).

## Results

| Graph | Qubits | G | Diff |
|-------|--------|---|------|
| Star | 4 | 0.500000 | 1.11e-16 |
| Line | 4 | 0.500000 | 1.11e-16 |
| Ring | 4 | 0.500000 | 1.11e-16 |

## Observations

1. **All graph states have G=0.5** for 4-qubit systems
2. **Graph topology does not affect G** for these simple graphs
3. **G=O holds exactly** for all topologies

## Note

These 4-qubit graph states are locally equivalent to the GHZ state, which
explains why they all have G=0.5.
