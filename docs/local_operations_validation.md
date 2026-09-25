# Local Operations Validation

## Date: 2026-09-25

## Purpose

Test G=O under local unitary operations.

## Setup

Apply random local unitaries U⊗V to Bell state |Φ⁺⟩.

## Results

| Operation | G | Diff |
|-----------|---|------|
| Initial | 0.5000 | 1.11e-16 |
| Local U1 | 0.5000 | 1.11e-16 |
| Local U2 | 0.5000 | 1.67e-16 |
| Local U3 | 0.5000 | 3.33e-16 |
| Local U4 | 0.5000 | 5.55e-17 |
| Local U5 | 0.5000 | 0.00e+00 |

## Observations

1. **G is invariant under local unitaries**
   - G remains 0.5 for all local operations

2. **G=O holds for all locally-transformed states**

## Conclusion

G=O is preserved under local unitary operations. The equality respects the
fundamental property that entanglement is invariant under local unitaries.
