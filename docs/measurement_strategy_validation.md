# Measurement Strategy Validation

## Date: 2026-09-25

## Purpose

Test G=O for different measurement strategies on the Bell state.

## Results

| Strategy | G | Diff |
|----------|---|------|
| Z-meas qubit 1 (\|0⟩) | 0.0000 | 0.00e+00 |
| Z-meas qubit 2 (\|0⟩) | 0.0000 | 0.00e+00 |
| Z-meas both (\|00⟩) | 0.0000 | 0.00e+00 |
| Bell-meas (\|Φ⁺⟩) | 0.5000 | 0.00e+00 |

## Observations

1. **Local measurements destroy entanglement** (G=0)
2. **Bell measurement preserves entanglement** (G=0.5)

## Conclusion

G=O correctly identifies that local measurements destroy entanglement while
Bell measurements preserve it.
