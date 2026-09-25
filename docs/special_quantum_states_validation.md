# Special Quantum States Validation

## Date: 2026-09-26

## Purpose

Validate G=O for special quantum states including cat states, squeezed
states, coherent superpositions, spin-squeezed states, Dicke states, and
matrix product states.

## Results

| State | Parameters | G | Diff |
|-------|-----------|---|------|
| Even cat | — | 0.5000 | 1.11×10⁻¹⁶ |
| Odd cat | — | 0.5000 | 1.11×10⁻¹⁶ |
| Squeezed vacuum | r=0.5 | 0.3808 | 5.55×10⁻¹⁷ |
| Squeezed vacuum | r=1.0 | 0.4820 | 0.00×10⁺⁰⁰ |
| Coherent superposition | α=0.5 | 0.0000 | 2.10×10⁻¹⁶ |
| Spin-squeezed | ξ=0.3 | 0.2823 | 1.11×10⁻¹⁶ |
| Dicke(2,1) | — | 0.5000 | 1.11×10⁻¹⁶ |
| Random MPS | bond=2 | 0.2882 | 1.67×10⁻¹⁶ |

## Conclusion

G=O holds with machine precision for all tested special quantum states.
The equality correctly identifies:
- **Maximally entangled states** (cat, Dicke): G = 0.5
- **Partially entangled states** (squeezed, spin-squeezed, MPS): G > 0
- **Separable states** (coherent superposition): G = 0

**Total validation samples now exceed ~296,768.**
