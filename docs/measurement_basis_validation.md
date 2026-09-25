# Measurement Basis Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states represented in different measurement bases.

## Setup

- Initial state: Bell state |Φ⁺⟩ in computational basis
- Transform to: X basis, Y basis, Bell basis

## Results

| Basis | G | Diff | Interpretation |
|-------|---|------|----------------|
| Computational | 0.500000 | 1.11e-16 | Standard |
| X | 0.500000 | 3.33e-16 | Entangled |
| Y | 0.500000 | 3.33e-16 | Entangled |
| Bell | 0.000000 | 4.60e-34 | Separable (diagonal) |

## Observations

1. **X and Y bases**: G remains 0.5
   - Bell state is still entangled in these bases

2. **Bell basis**: G becomes 0
   - State is diagonal in this basis (classically correlated)
   - This is expected: Bell states are product states in the Bell basis

3. **G=O holds exactly** in all bases

## Conclusion

G=O is basis-independent. The equality holds regardless of the measurement
basis used to represent the state.
