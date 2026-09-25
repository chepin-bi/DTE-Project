# Time-Evolved State Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for states evolved under arbitrary Hamiltonians (unitary
evolution).

## Setup

- Initial state: Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
- Hamiltonian: Random Hermitian H ∈ ℂ⁴ˣ⁴
- Evolution: ρ(t) = e^(-iHt) ρ(0) e^(iHt)

## Results

| Time | G | Diff |
|------|---|------|
| 0.0 | 0.500000 | 1.11e-16 |
| 0.1 | 0.468379 | 0.00e+00 |
| 0.5 | 0.297631 | 1.11e-16 |
| 1.0 | 0.170670 | 2.22e-16 |
| 2.0 | 0.376546 | 6.11e-16 |
| 5.0 | 0.203748 | 1.78e-15 |

## Conclusion

G=O holds exactly for all time-evolved states under unitary dynamics. The
equality is preserved under Hamiltonian evolution, consistent with the
unitary invariance of the trace norm.

Note: G changes with time (entanglement oscillates), but G=O holds at all
times.
