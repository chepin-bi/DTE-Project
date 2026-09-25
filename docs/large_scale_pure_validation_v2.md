# Large-Scale Pure State Validation v2

## Date: 2026-09-26

## Purpose

Large-scale validation of G=O for pure states across multiple dimensions.

## Results

| Dimensions | Samples | Pass Rate | Max Diff | Time |
|-----------|---------|-----------|----------|------|
| 2×2 | 2,000 | 2000/2000 (100%) | 7.22×10⁻¹⁶ | 0.2s |
| 3×3 | 1,500 | 1500/1500 (100%) | 6.66×10⁻¹⁶ | 0.2s |
| 2×3 | 1,000 | 1000/1000 (100%) | 7.77×10⁻¹⁶ | 0.1s |
| 4×4 | 500 | 500/500 (100%) | 6.66×10⁻¹⁶ | 0.1s |

### Summary

| Metric | Value |
|--------|-------|
| Total samples | **5,000** |
| Pass rate | **5,000/5,000 (100%)** |
| Maximum difference | **7.77×10⁻¹⁶** |
| Total time | **0.7s** |

## Conclusion

G=O holds with machine precision for all 5,000 tested pure states across
four dimension combinations. The equality is exact and computationally
efficient.

**Total validation samples now exceed ~314,880.**
