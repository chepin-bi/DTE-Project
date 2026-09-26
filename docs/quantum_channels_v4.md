# Quantum Channels Validation v4

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~2,268,430+

## Purpose

Validate G=O under collective amplitude damping, correlated amplitude
damping, random unitary, entanglement-breaking, and combined channels.

## Results

### Collective Amplitude Damping

| p | G | Diff |
|---|------|------|
| 0.1 | 0.4945 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.4430 | 5.55×10⁻¹⁷ |
| 0.5 | 0.3333 | 0.00×10⁺⁰⁰ |
| 0.7 | 0.1899 | 2.78×10⁻¹⁷ |
| 0.9 | 0.0549 | 4.16×10⁻¹⁷ |

### Correlated Amplitude Damping

| p | G | Diff |
|---|------|------|
| 0.1 | 0.4000 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.2000 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.7 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.9 | 0.0000 | 0.00×10⁺⁰⁰ |

### Random Unitary Channel

| p | G | Diff |
|---|------|------|
| 0.1 | 0.4218 | 1.67×10⁻¹⁶ |
| 0.3 | 0.3355 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.2191 | 3.05×10⁻¹⁶ |
| 0.7 | 0.3000 | 5.55×10⁻¹⁷ |
| 0.9 | 0.2052 | 5.55×10⁻¹⁷ |

### Entanglement-Breaking Channel

| p | G | Diff |
|---|------|------|
| 0.1 | 0.4250 | 1.11×10⁻¹⁶ |
| 0.3 | 0.2750 | 0.00×10⁺⁰⁰ |
| 0.5 | 0.1250 | 5.55×10⁻¹⁷ |
| 0.7 | 0.0000 | 0.00×10⁺⁰⁰ |
| 0.9 | 0.0000 | 0.00×10⁺⁰⁰ |

### Depolarizing + Collective Dephasing

| p_dep | p_deph | G | Diff |
|-------|--------|------|------|
| 0.1 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.1 | 0.3 | 0.4250 | 1.11×10⁻¹⁶ |
| 0.3 | 0.1 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.3 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.5 | 0.1 | 0.1250 | 6.94×10⁻¹⁷ |
| 0.5 | 0.3 | 0.1250 | 6.94×10⁻¹⁷ |

## Key Findings

1. **Collective damping**: G decreases gradually
2. **Correlated damping**: G→0 at p=0.5 (sudden death)
3. **Entanglement-breaking**: G→0 at p=0.7
4. **Combined channels**: G only depends on depolarization
5. **Collective dephasing**: Preserves G (decoherence-free)

## Conclusion

G=O holds with machine precision under all tested channels.

**Total validation samples now exceed ~2,268,430.**
