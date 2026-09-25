# Multiple Negative Eigenvalues Validation

## Date: 2026-09-25

## Purpose

Test G=O for states whose partial transpose has multiple negative
eigenvalues.

## Results

### 3×3 Pure States

| Sample | G | n_neg | Diff |
|--------|---|-------|------|
| 1 | 0.5737 | 3 | 4.44e-16 |
| 2 | 0.7311 | 3 | 3.33e-16 |
| 3 | 0.5559 | 3 | 3.33e-16 |
| 4 | 0.7416 | 3 | 1.11e-16 |
| 5 | 0.6831 | 3 | 0.00e+00 |

### 4×4 Pure States

| Sample | G | n_neg | Diff |
|--------|---|-------|------|
| 1 | 0.8233 | 6 | 2.22e-16 |
| 2 | 1.0971 | 6 | 2.22e-16 |
| 3 | 0.9052 | 6 | 0.00e+00 |
| 4 | 0.8237 | 6 | 0.00e+00 |
| 5 | 0.9423 | 6 | 0.00e+00 |

## Key Findings

1. **3×3 pure states**: PT has exactly 3 negative eigenvalues
2. **4×4 pure states**: PT has exactly 6 negative eigenvalues
3. **G=O holds exactly** regardless of the number of negative eigenvalues

## Theoretical Note

For a d×d pure state, the partial transpose can have at most d(d−1)/2
negative eigenvalues. The number of negative eigenvalues depends on the
Schmidt rank and coefficients, but G=O is independent of this structure.

## Conclusion

G=O holds exactly even when the partial transpose has multiple negative
eigenvalues. The equality is robust against the complexity of the
entanglement structure.
