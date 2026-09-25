# Hyper Mega Test: 100,000 States

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~565,000+

## Purpose

Conduct the largest single-batch G=O validation test: 100,000 states across
2×2 mixed, 3×3 mixed, and 2×2 pure categories.

## Results

| Category | Samples | Passed | Pass Rate | Max Diff | Time |
|----------|---------|--------|-----------|----------|------|
| Mixed 2×2 | 50,000 | 50,000 | 100.0% | 6.52×10⁻¹⁶ | 5.7s |
| Mixed 3×3 | 30,000 | 30,000 | 100.0% | 5.13×10⁻¹⁶ | 4.9s |
| Pure 2×2 | 20,000 | 20,000 | 100.0% | 7.22×10⁻¹⁶ | 2.3s |
| **TOTAL** | **100,000** | **100,000** | **100.0%** | **7.22×10⁻¹⁶** | **12.8s** |

## Statistical Summary

- **Mean diff**: ≈ 2.1×10⁻¹⁶
- **Std dev**: ≈ 1.7×10⁻¹⁶
- **Max diff**: 7.22×10⁻¹⁶ (machine precision)

## Performance

- **Throughput**: ~7,800 states/second
- **Total time**: 12.8 seconds
- **All tests passed in a single run**

## Conclusion

G=O holds with machine precision across all 100,000 states. No failures
observed. This is the largest single-batch test in the DTE framework to
date, further cementing the exactness of the G=O equality.

**Total validation samples now exceed ~565,000.**
