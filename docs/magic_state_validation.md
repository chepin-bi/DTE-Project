# Magic State Validation

## Date: 2026-09-25

## Purpose

Test G=O for magic states (non-stabilizer states used in fault-tolerant
quantum computation).

## Results

### Magic States

| State | G | Diff |
|-------|---|------|
| T⊗T | 0.0000 | 8.13e-17 |
| H⊗H | 0.0000 | 8.13e-17 |
| Magic⊗Magic* | 0.0000 | 2.03e-17 |

## Observations

1. **Magic product states are separable** (G=0)
   - Expected for product states

2. **G=O holds exactly** for magic states

## Conclusion

G=O applies to magic states. While magic states are non-stabilizer, product
magic states remain separable and satisfy G=O=0.
