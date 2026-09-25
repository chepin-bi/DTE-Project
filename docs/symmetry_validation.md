# Symmetry Validation

## Date: 2026-09-25

## Purpose

Test G=O for states with different symmetries.

## Results

| Symmetry | G | Diff |
|----------|---|------|
| Symmetric (Bell) | 0.5000 | 1.11e-16 |
| Anti-symmetric | 0.5000 | 1.11e-16 |
| Permutation symmetric | 0.0000 | 1.06e-16 |
| Real | 0.5000 | 1.11e-16 |
| Imaginary | 0.5000 | 1.11e-16 |

## Conclusion

G=O holds for states with all tested symmetries. The equality correctly
identifies that the permutation-symmetric state |++⟩ is separable (G=0),
while Bell and anti-symmetric states are entangled (G=0.5).
