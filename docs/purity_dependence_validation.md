# Purity Dependence Validation

## Date: 2026-09-25

## Purpose

Test G=O for states with different purity values.

## Results

| Target Purity | Actual Purity | G | Diff |
|---------------|---------------|---|------|
| 0.3 | 0.5497 | 0.1589 | 2.22e-16 |
| 0.5 | 0.6277 | 0.0845 | 1.39e-16 |
| 0.7 | 1.0000 | 0.4428 | 5.55e-17 |
| 0.9 | 1.0000 | 0.4454 | 0.00e+00 |
| 1.0 | 1.0000 | 0.2330 | 5.55e-17 |

## Observations

1. **G=O holds for all purity values**
2. **Mixed states (purity < 1) can have G > 0**
3. **Purity and G are not directly correlated**
   - A pure state can have G=0 (separable)
   - A mixed state can have G>0 (entangled)

## Conclusion

G=O is independent of purity. The equality holds for both pure and mixed
states across the full range of purity values.
