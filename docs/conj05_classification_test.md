# CONJ-05: DTE Triple as Entanglement Classifier

## Date: 2026-09-25

## Investigation

Can the DTE triple (G, I, O) distinguish different entanglement classes?

## Test Results (4-Qubit States, AB|CD Bipartition)

| State | G | I | O | I/G² |
|-------|---|---|---|------|
| GHZ₄ | 0.5000 | 2.0000 | 0.5000 | 8.00 |
| Cluster₄ | 0.5000 | 2.0000 | 0.5000 | 8.00 |
| Dicke₄² | 0.8333 | 2.5033 | 0.8333 | 3.60 |
| Random pure | 1.1667 | 3.1073 | 1.1667 | 2.28 |

## Observations

1. **GHZ₄ and Cluster₄ have identical signatures** (G=0.5, I=2.0)
   - These states are locally equivalent under Clifford operations
   - The DTE triple cannot distinguish locally equivalent states

2. **Dicke₄² has a distinct signature** (G=0.833, I=2.503)
   - Higher G reflects stronger bipartite entanglement
   - Different I/G² ratio (3.60 vs 8.00)

3. **Random pure states span a range** of (G, I) values
   - G ranges from 0 to ~1.5 for 4-qubit states
   - I ranges from 0 to ~4
   - The I/G² ratio varies widely

## Implications

1. **Local equivalence limitation**: States related by local unitaries
   have identical DTE triples (by construction, since G and I are
   LOCC monotones).

2. **Partial classification**: The DTE triple can distinguish some
   entanglement classes (e.g., GHZ vs Dicke) but not all (e.g., GHZ
   vs Cluster).

3. **Continuous spectrum**: Random pure states populate a continuous
   region in (G, I) space, suggesting entanglement is not discrete.

## Conclusion

The DTE triple provides **partial classification** of entanglement:
- Can distinguish broad classes (GHZ-like vs Dicke-like)
- Cannot distinguish locally equivalent states
- May require additional invariants for complete classification

## Next Steps

- Test W states for higher party counts
- Investigate if I/G² ratio is a class invariant
- Explore additional measures for complete classification
