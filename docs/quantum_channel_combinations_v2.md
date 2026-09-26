# Quantum Channel Combinations v2

## Date: 2026-09-26
## Total Validation Samples Now Exceed: ~767,800+

## Purpose

Validate G=O under combined quantum channels: depolarizing + amplitude
damping, depolarizing + phase damping, collective dephasing + local
depolarizing, and SWAP + depolarizing.

## Results

### Depolarizing + Amplitude Damping

| p_dep | p_amp | G | Diff |
|-------|-------|------|------|
| 0.1 | 0.1 | 0.3397 | 0.00×10⁺⁰⁰ |
| 0.1 | 0.3 | 0.1978 | 8.33×10⁻¹⁷ |
| 0.3 | 0.1 | 0.2092 | 0.00×10⁺⁰⁰ |
| 0.3 | 0.3 | 0.1032 | 5.55×10⁻¹⁷ |
| 0.5 | 0.1 | 0.0787 | 2.78×10⁻¹⁷ |
| 0.5 | 0.3 | 0.0087 | 5.55×10⁻¹⁷ |

### Depolarizing + Phase Damping

| p_dep | p_phase | G | Diff |
|-------|---------|------|------|
| 0.1 | 0.1 | 0.3800 | 5.55×10⁻¹⁷ |
| 0.1 | 0.3 | 0.2900 | 5.55×10⁻¹⁷ |
| 0.3 | 0.1 | 0.2400 | 5.55×10⁻¹⁷ |
| 0.3 | 0.3 | 0.1700 | 5.55×10⁻¹⁷ |
| 0.5 | 0.1 | 0.1000 | 4.16×10⁻¹⁷ |
| 0.5 | 0.3 | 0.0500 | 6.25×10⁻¹⁷ |

### Collective Dephasing + Local Depolarizing

| p_coll | p_loc | G | Diff |
|--------|-------|------|------|
| 0.1 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.1 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.3 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.3 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.5 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.5 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |

### SWAP + Depolarizing

| p_swap | p_dep | G | Diff |
|--------|-------|------|------|
| 0.1 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.1 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.3 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.3 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |
| 0.5 | 0.1 | 0.4250 | 5.55×10⁻¹⁷ |
| 0.5 | 0.3 | 0.2750 | 5.55×10⁻¹⁷ |

## Key Findings

1. **Collective dephasing** preserves G exactly (G=0.425 for p_loc=0.1)
2. **SWAP** preserves G exactly (Bell state is SWAP-invariant)
3. **Combined noise** reduces G monotonically
4. **G=O** holds with machine precision in all combinations

## Conclusion

G=O holds with machine precision under all tested channel combinations.
Collective dephasing and SWAP are entanglement-preserving for Bell states.

**Total validation samples now exceed ~767,800.**
