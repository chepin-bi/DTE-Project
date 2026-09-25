# Large-Scale Statistical Validation

## Date: 2026-09-25

## Purpose

Large-scale statistical validation of G=O for random mixed states.

## Results

### 500 Random 2×2 Mixed States

| Metric | Value |
|--------|-------|
| Pass rate | 500/500 (100%) |
| Maximum difference | 5.55×10⁻¹⁶ |
| Time | 0.1s |

### 200 Random 3×3 Mixed States

| Metric | Value |
|--------|-------|
| Pass rate | 200/200 (100%) |
| Maximum difference | 3.54×10⁻¹⁶ |
| Time | 0.0s |

## Conclusion

G=O holds with machine precision for all 700 tested random mixed states.
The maximum observed difference (5.55×10⁻¹⁶) is within numerical round-off
error. Total validation samples now exceed ~280,000.
