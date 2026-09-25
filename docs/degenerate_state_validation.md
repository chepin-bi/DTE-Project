# Degenerate State Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states of different ranks (degenerate eigenvalues).

## Results

### Rank-1 States (Pure)

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.249096 | 2.78e-17 |
| 2 | 0.323429 | 5.55e-17 |
| 3 | 0.359364 | 1.11e-16 |
| 4 | 0.243765 | 1.94e-16 |
| 5 | 0.325902 | 2.78e-16 |

**Pass rate: 5/5 (100%)**

### Rank-2 States (Mixed)

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.237438 | 8.33e-17 |
| 2 | 0.194428 | 1.11e-16 |
| 3 | 0.090766 | 1.39e-17 |
| 4 | 0.055653 | 3.19e-16 |
| 5 | 0.069828 | 2.36e-16 |

**Pass rate: 5/5 (100%)**

### Rank-3 States (Mixed)

| Sample | G | Diff |
|--------|---|------|
| 1 | 0.031117 | 4.16e-17 |
| 2 | 0.055527 | 2.08e-16 |
| 3 | 0.047900 | 1.87e-16 |

**Pass rate: 3/3 (100%)**

## Conclusion

G=O holds exactly for states of all ranks (1, 2, 3) in 2×2 systems. The
equality is independent of the rank or degeneracy structure of the density
matrix.

## Combined Evidence

| Test Type | Samples | Pass Rate |
|-----------|---------|-----------|
| Pure real | 100+ | 100% |
| Pure complex | 10 | 100% |
| Mixed random | 100+ | 100% |
| Rank-1 | 5 | 100% |
| Rank-2 | 5 | 100% |
| Rank-3 | 3 | 100% |
| Multi-party | 278,700+ | 99.61% |

Total: ~278,828 samples, **99.61% pass rate**
