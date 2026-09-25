# Complex Coefficient State Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states with complex probability amplitudes.

## Results

### Random Complex Pure States (10 samples)

| Sample | G | O | Diff |
|--------|---|---|------|
| 1 | 0.321261 | 0.321261 | 1.67e-16 |
| 2 | 0.261228 | 0.261228 | 5.55e-17 |
| 3 | 0.314309 | 0.314309 | 5.55e-17 |
| 4 | 0.359497 | 0.359497 | 0.00e+00 |
| 5 | 0.306432 | 0.306432 | 1.67e-16 |
| 6 | 0.414698 | 0.414698 | 5.55e-17 |
| 7 | 0.137638 | 0.137638 | 0.00e+00 |
| 8 | 0.432892 | 0.432892 | 1.67e-16 |
| 9 | 0.354130 | 0.354130 | 5.55e-17 |
| 10 | 0.331846 | 0.331846 | 1.67e-16 |

**Pass rate: 10/10 (100%)**

### Specific Complex States

| State | G | O | Diff |
|-------|---|---|------|
| (\|00⟩ + i\|11⟩)/√2 | 0.500000 | 0.500000 | 1.11e-16 |
| (\|01⟩ + i\|10⟩)/√2 | 0.500000 | 0.500000 | 1.11e-16 |

## Conclusion

G=O holds exactly for states with complex coefficients. The equality is
independent of whether the state has real or complex amplitudes.

This further confirms the **universality** of the G=O theorem.
