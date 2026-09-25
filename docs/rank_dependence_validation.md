# Rank Dependence Validation

## Date: 2026-09-25

## Purpose

Test G=O for mixed states with different ranks.

## Results

| Target Rank | Actual Rank | G | Diff |
|-------------|-------------|---|------|
| 1 | 1 | 0.1235 | 0.00e+00 |
| 2 | 2 | 0.2022 | 8.33e-17 |
| 3 | 3 | 0.1178 | 5.55e-17 |
| 4 | 4 | 0.0370 | 2.78e-17 |

## Observations

1. **G=O holds for all ranks**
2. **G does not monotonically increase with rank**
   - Rank-2 state has higher G than rank-1
   - But rank-4 has lower G than rank-3
   - G depends on specific state, not just rank

## Conclusion

G=O is independent of density matrix rank. The equality holds for rank-1
(pure) through rank-4 (maximally mixed) states.
