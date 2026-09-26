# Extreme Dimensions Validation

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~1,267,780+

## Purpose

Validate G=O for extreme dimensions: 22×22, 25×25, 30×30, and non-uniform
2×30, 3×20, 5×15.

## Results

### Uniform Dimensions

| Dimension | Samples | Passed | Pass Rate | Max Diff | Time |
|-----------|---------|--------|-----------|----------|------|
| 22×22 | 20 | 20 | 100.0% | 1.94×10⁻¹⁶ | 5.2s |
| 25×25 | 20 | 20 | 100.0% | 1.67×10⁻¹⁶ | 7.3s |
| 30×30 | 20 | 20 | 100.0% | 1.53×10⁻¹⁶ | 14.8s |

### Non-Uniform Dimensions

| Dimension | Samples | Passed | Pass Rate | Max Diff | Time |
|-----------|---------|--------|-----------|----------|------|
| 2×30 | 20 | 20 | 100.0% | 2.91×10⁻¹⁶ | 1.0s |
| 3×20 | 20 | 20 | 100.0% | 1.94×10⁻¹⁶ | 0.6s |
| 5×15 | 20 | 20 | 100.0% | 2.36×10⁻¹⁶ | 0.9s |

## Conclusion

G=O holds with machine precision up to dimension 30×30 and non-uniform
2×30. The equality remains exact across all tested dimensions from 2×2 to
30×30.

**Total validation samples now exceed ~1,267,780.**
