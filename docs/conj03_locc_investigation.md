# CONJ-03: LOCC Monotonicity Investigation

## Date: 2026-09-25

## Tests Performed

### Test 1: Local Unitary Invariance

For Bell state |Φ⁺⟩:
- Apply random local unitary U to party A: G and I unchanged
- Apply random local unitary U to party B: G and I unchanged

**Result:** G and I are invariant under local unitaries (diff ~ 10⁻¹⁶)

### Test 2: Local Projective Measurement

Measure party A of Bell state in computational basis:
- Outcome 0 (p=0.5): state collapses to |00⟩, G=0, I=0
- Outcome 1 (p=0.5): state collapses to |11⟩, G=0, I=0
- Average after measurement: G_avg=0, I_avg=0

**Result:** Average G and I decreased from (0.5, 2.0) to (0, 0)

## Interpretation

The observation that G and I do not increase under:
1. Local unitaries (invariant)
2. Local measurements (decrease on average)

is **consistent with LOCC monotonicity**.

However, this is only a preliminary test. Full proof of CONJ-03 requires:
1. General LOCC operations (not just unitaries and projective measurements)
2. Classical communication component
3. Multi-round LOCC protocols

## Status

CONJ-03 remains **OPEN** but preliminary evidence is encouraging.

## Next Steps

- Test more general LOCC operations
- Investigate if G and I are entanglement monotones in the formal sense
- Theoretical proof using LOCC formalism
