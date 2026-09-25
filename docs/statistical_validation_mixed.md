# Statistical Validation: Random Mixed States

## Date: 2026-09-25

## Purpose

Statistically validate G=O for random mixed states.

## Results

### 2×2 Random Mixed States (50 samples)

| Metric | Value |
|--------|-------|
| Max G | 0.2566 |
| Min G | 0.0000 |
| Max diff | 3.82×10⁻¹⁶ |
| Pass rate | 50/50 (100%) |

### 3×3 Random Mixed States (20 samples)

| Metric | Value |
|--------|-------|
| Max G | 0.7799 |
| Min G | 0.0000 |
| Max diff | 2.36×10⁻¹⁶ |
| Pass rate | 20/20 (100%) |

## Conclusion

G=O holds with machine precision for all tested random mixed states. The
maximum observed difference (3.82×10⁻¹⁶) is within numerical round-off error.
