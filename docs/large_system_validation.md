# Large System Validation (10×10)

## Date: 2026-09-25

## Purpose

Test G=O for large-dimensional systems (10×10, dimension 100).

## Results

| State | G | Diff | Time |
|-------|---|------|------|
| Maximally entangled | 4.5000 | 8.88e-16 | 0.001s |
| Random pure | 3.0681 | 0.00e+00 | 0.002s |
| Random mixed | 0.0748 | 9.71e-17 | 0.026s |

## Observations

1. **G=O holds exactly** even for 100-dimensional density matrices
2. **Computation time** is negligible (< 0.03s) for all cases
3. **Maximally entangled**: G = (10−1)/2 = 4.5, as expected

## Conclusion

The G=O equality scales to large systems without numerical issues. The
eigenvalue computation remains stable for dimension 100.
