# Quantum Operations Validation v2

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,267,980+

## Purpose

Validate G=O under local unitary, CNOT, Hadamard+CNOT, Toffoli-like, and
random Clifford operations.

## Results

### Local Unitary Operations

| θ | G | Diff |
|---|------|------|
| 0.0000 | 0.5000 | 1.11×10⁻¹⁶ |
| 0.7854 | 0.5000 | 1.11×10⁻¹⁶ |
| 1.5708 | 0.5000 | 1.11×10⁻¹⁶ |
| 2.3562 | 0.5000 | 1.11×10⁻¹⁶ |
| 3.1416 | 0.5000 | 1.11×10⁻¹⁶ |

### CNOT Operations

| p | G | Diff |
|---|------|------|
| 0.0 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.0000 | 1.59×10⁻¹⁷ |
| 0.5 | 0.0000 | 1.11×10⁻¹⁶ |
| 0.7 | 0.0000 | 0.00×10⁺⁰⁰ |
| 1.0 | 0.0000 | 0.00×10⁺⁰⁰ |

### Hadamard + CNOT (Bell Generation)

| p | G | Diff |
|---|------|------|
| 0.0 | 0.5000 | 1.11×10⁻¹⁶ |
| 0.5 | 0.5000 | 1.11×10⁻¹⁶ |
| 1.0 | 0.5000 | 1.11×10⁻¹⁶ |

### Toffoli-like Operations

| p | G | Diff |
|---|------|------|
| 0.0 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.5000 | 1.11×10⁻¹⁶ |
| 1.0 | 0.0000 | 0.00×10⁺⁰⁰ |

### Random Clifford Operations

| Operation | G | Diff |
|-----------|------|------|
| Clifford 1 | 0.4943 | 2.78×10⁻¹⁶ |
| Clifford 2 | 0.4603 | 1.67×10⁻¹⁶ |
| Clifford 3 | 0.3651 | 1.67×10⁻¹⁶ |
| Clifford 4 | 0.2568 | 5.55×10⁻¹⁷ |
| Clifford 5 | 0.2832 | 1.11×10⁻¹⁶ |

## Key Findings

1. **Local unitary**: G invariant (LU invariance confirmed)
2. **CNOT on product states**: G remains 0
3. **Hadamard+CNOT**: Generates Bell states with G=0.5
4. **Toffoli**: G=0.5 for superposition states
5. **Clifford**: Preserves G=O exactness

## Conclusion

G=O holds with machine precision under all tested quantum operations.
Local unitary invariance is numerically confirmed.

**Total validation samples now exceed ~2,267,980.**
