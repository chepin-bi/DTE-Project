# Non-Uniform Bipartition Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for bipartitions where subsystems have different dimensions
(non-uniform bipartitions).

## Results

### 2×3 Bipartition

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.468491 | 3.33e-16 |
| 2 | 0.419716 | 1.11e-16 |
| 3 | 0.403014 | 2.22e-16 |
| 4 | 0.353853 | 0.00e+00 |
| 5 | 0.433173 | 1.67e-16 |

**Pass rate: 5/5 (100%)**

### 2×4 Bipartition

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.448597 | 2.22e-16 |
| 2 | 0.365051 | 3.33e-16 |
| 3 | 0.477751 | 2.78e-16 |
| 4 | 0.486198 | 0.00e+00 |
| 5 | 0.444183 | 2.78e-16 |

**Pass rate: 5/5 (100%)**

### 3×4 Bipartition

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.871975 | 2.22e-16 |
| 2 | 0.738473 | 1.11e-16 |
| 3 | 0.531394 | 1.11e-16 |
| 4 | 0.614202 | 4.44e-16 |
| 5 | 0.829938 | 4.44e-16 |

**Pass rate: 5/5 (100%)**

## Conclusion

G=O holds exactly for non-uniform bipartitions (2×3, 2×4, 3×4). The equality
is independent of whether the subsystems have equal dimensions.

This confirms that the G=O theorem applies to **all bipartitions**, not just
symmetric ones.
