# Massive High-Dimensional Saturation Test

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~567,700+

## Purpose

Extend G=O validation to dimensions up to 20×20, non-uniform up to 2×20,
plus structured randomness and pure state batches.

## Results

### Uniform Dimensions

| Dimension | Samples | Passed | Pass Rate | Max Diff | Time |
|-----------|---------|--------|-----------|----------|------|
| 16×16 | 50 | 50 | 100.0% | 2.36×10⁻¹⁶ | 4.8s |
| 17×17 | 50 | 50 | 100.0% | 2.22×10⁻¹⁶ | 5.6s |
| 18×18 | 50 | 50 | 100.0% | 2.08×10⁻¹⁶ | 8.3s |
| 19×19 | 50 | 50 | 100.0% | 1.80×10⁻¹⁶ | 10.2s |
| 20×20 | 50 | 50 | 100.0% | 2.08×10⁻¹⁶ | 10.4s |

### Non-Uniform Dimensions

| Dimension | Samples | Passed | Pass Rate | Max Diff | Time |
|-----------|---------|--------|-----------|----------|------|
| 2×20 | 50 | 50 | 100.0% | 1.80×10⁻¹⁶ | 0.0s |
| 3×15 | 50 | 50 | 100.0% | 2.64×10⁻¹⁶ | 0.1s |
| 4×12 | 50 | 50 | 100.0% | 2.22×10⁻¹⁶ | 0.1s |
| 5×10 | 50 | 50 | 100.0% | 2.91×10⁻¹⁶ | 1.7s |
| 6×8 | 50 | 50 | 100.0% | 2.64×10⁻¹⁶ | 0.1s |

### Additional Tests

| Category | Samples | Passed | Pass Rate | Max Diff | Time |
|----------|---------|--------|-----------|----------|------|
| Pure 2×2 | 1,000 | 1,000 | 100.0% | 7.22×10⁻¹⁶ | 0.1s |
| Structured 2×2 | 500 | 500 | 100.0% | 4.44×10⁻¹⁶ | 0.1s |

### Batch Summary

| Metric | Value |
|--------|-------|
| Total samples | 2,000 |
| Passed | 2,000 |
| Pass rate | 100.0% |
| Maximum diff | 7.22×10⁻¹⁶ |
| Total time | 41.6s |

## Conclusion

G=O holds with machine precision up to dimension 20×20 and non-uniform
2×20. The equality remains exact across all tested dimensions from 2×2 to
20×20. Structured randomness (small off-diagonal perturbations) also
preserves G=O exactness.

**Total validation samples now exceed ~567,700.**
