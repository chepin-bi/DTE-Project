# Spectrum Dependence Validation

## Date: 2026-09-25

## Purpose

Test G=O for mixed states with different eigenvalue spectra.

## Results

| Spectrum | G | Diff |
|----------|---|------|
| Uniform | 0.0000 | 0.00e+00 |
| Degenerate | 0.0437 | 2.71e-16 |
| Dominant | 0.0469 | 3.68e-16 |
| Power law | 0.1540 | 2.22e-16 |
| Exponential | 0.0453 | 2.78e-17 |

## Observations

1. **Uniform spectrum (I/4)**: G=0 (separable)
2. **Non-uniform spectra**: G>0 (entangled)
3. **G=O holds for all spectra**

## Conclusion

G=O is independent of the eigenvalue spectrum. The equality holds for
uniform, degenerate, dominant, power-law, and exponential spectra.
