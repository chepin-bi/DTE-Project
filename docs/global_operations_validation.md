# Global Operations Validation

## Date: 2026-09-25

## Purpose

Test G=O under global unitary operations.

## Setup

Apply random global unitaries to separable state |00⟩.

## Results

| Operation | G | Diff |
|-----------|---|------|
| Initial | 0.0000 | 0.00e+00 |
| Global U1 | 0.3165 | 2.78e-16 |
| Global U2 | 0.1454 | 3.33e-16 |
| Global U3 | 0.2448 | 1.94e-16 |
| Global U4 | 0.4182 | 0.00e+00 |
| Global U5 | 0.2712 | 1.11e-16 |

## Observations

1. **Global unitaries create entanglement**
   - G increases from 0 to >0

2. **G=O holds for all globally-transformed states**

## Conclusion

G=O is preserved under global unitary operations. The equality correctly
tracks entanglement generation by non-local operations.
