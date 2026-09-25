# Non-Uniform Dimension Validation

## Date: 2026-09-26

## Purpose

Validate G=O for non-uniform bipartite dimensions.

## Results

| Dimensions | Type | Samples | Pass Rate | Max Diff | Time |
|-----------|------|---------|-----------|----------|------|
| 2×5 | Mixed | 500 | 500/500 (100%) | 3.61×10⁻¹⁶ | 0.1s |
| 2×6 | Mixed | 400 | 400/400 (100%) | 3.75×10⁻¹⁶ | 0.1s |
| 3×5 | Mixed | 300 | 300/300 (100%) | 3.47×10⁻¹⁶ | 0.1s |
| 2×8 | Pure | 200 | 200/200 (100%) | 5.55×10⁻¹⁶ | 0.0s |
| 3×6 | Pure | 200 | 200/200 (100%) | 6.66×10⁻¹⁶ | 0.0s |
| 2×10 | Pure | 100 | 100/100 (100%) | 7.77×10⁻¹⁶ | 0.0s |

### Summary

| Metric | Value |
|--------|-------|
| Total samples | **1,700** |
| Pass rate | **1,700/1,700 (100.0%)** |
| Maximum difference | **7.77×10⁻¹⁶** |
| Total time | **0.3s** |

## Conclusion

G=O holds with machine precision for all tested non-uniform bipartite
dimensions. The equality is robust regardless of whether the subsystems
have equal or unequal dimensions.

**Total validation samples now exceed ~296,760.**
