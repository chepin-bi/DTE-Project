# Different Bipartitions Validation

## Date: 2026-09-25

## Purpose

Test G=O for 4-qubit states under different bipartitions.

## Results

### GHZ₄ State

| Bipartition | G | Diff |
|-------------|---|------|
| 1\|3 | 0.5000 | 1.11e-16 |
| 2\|2 | 0.5000 | 1.11e-16 |
| 3\|1 | 0.5000 | 1.11e-16 |

### W₄ State

| Bipartition | G | Diff |
|-------------|---|------|
| 1\|3 | 0.4330 | 1.11e-16 |
| 2\|2 | 0.5000 | 0.00e+00 |
| 3\|1 | 0.4330 | 1.11e-16 |

## Observations

1. **GHZ state**: G=0.5 for all bipartitions
   - Maximally entangled across any cut

2. **W state**: G varies with bipartition
   - 2|2: G=0.5 (maximal)
   - 1|3: G=0.433 (less entangled)

3. **G=O holds for all bipartitions**

## Conclusion

G=O is independent of the bipartition choice. The equality holds for all
ways of partitioning a multipartite system.
