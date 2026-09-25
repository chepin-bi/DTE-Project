# CONJ-05: Extended Multi-Party Classification Investigation

## Date: 2026-09-25

## Summary

The DTE triple (G, I, O) provides **partial classification** of entanglement
classes. The key discriminator is the **I/G² ratio**.

## Key Findings

### 1. GHZ/Cluster States

| State | G | I | I/G² | Classification |
|-------|---|---|------|----------------|
| GHZ₄ | 0.5000 | 2.0000 | 8.00 | Saturates T2 |
| Cluster₄ | 0.5000 | 2.0000 | 8.00 | Saturates T2 |

**Observation:** GHZ and Cluster are **indistinguishable** by DTE triple
(but they are locally equivalent under Clifford operations).

### 2. W States

| n | Bipartition | G | I | I/G² |
|---|-------------|---|---|------|
| 3 | 1\|2 | 0.4714 | 1.8366 | 8.26 |
| 4 | 2\|2 | 0.5000 | 2.0000 | 8.00 |
| 5 | 2\|3 | 0.4899 | 1.9419 | 8.09 |
| 6 | 3\|3 | 0.5000 | 2.0000 | 8.00 |

**Observation:** W states have I/G² ≈ 8.0-8.3, **near saturation**.

### 3. Dicke States

| n | k | G | I | I/G² |
|---|---|---|---|------|
| 4 | 1 | 0.5000 | 2.0000 | 8.00 |
| 4 | 2 | 0.8333 | 2.5033 | 3.60 |
| 5 | 2 | 0.8424 | 2.5909 | 3.65 |
| 6 | 2 | 0.8928 | 2.7419 | 3.44 |
| 6 | 3 | 1.1000 | 2.9380 | 2.43 |

**Observation:** Dicke(n,k) with k≥2 have I/G² ≈ 2.4-3.7, **well below
saturation**.

### 4. Random Pure States

Variable I/G², typically 2.0-3.0 for 4-qubit systems.

## Classification Hierarchy

Based on I/G² ratio (for symmetric bipartitions):

| Class | I/G² Range | Entanglement Type |
|-------|------------|-------------------|
| GHZ/Cluster/W | ≈ 8.0 | Saturation-type |
| Dicke(k≥2) | 2.4-3.7 | Sub-saturation |
| Random pure | 2.0-8.0 | Variable |
| Product | N/A (G=0) | Separable |

## Conclusion

The DTE triple **partially classifies** entanglement:

1. **Can distinguish:** GHZ-type vs Dicke-type vs separable
2. **Cannot distinguish:** GHZ vs Cluster (locally equivalent)
3. **Cannot distinguish:** GHZ vs W (both saturate T2)

The I/G² ratio is a **coarse classifier**: it separates broad categories
but does not provide fine-grained classification.

## Theoretical Interpretation

States that saturate Theorem 2 (I/G² = 8.0) are "maximally entangled"
with respect to the information-entanglement tradeoff. These include:
- GHZ states (genuine multipartite)
- Bell states (bipartite maximally entangled)
- W states (robust entanglement)

States with I/G² < 8.0 have "excess entanglement" that is not captured
by mutual information, suggesting more complex entanglement structures.

## Status Update

CONJ-05: 🟡 **PARTIALLY RESOLVED**
- DTE triple provides coarse classification
- I/G² ratio is a useful discriminator
- Fine-grained classification requires additional invariants

---

*DTE Framework v3.2.0 | 2026-09-25*
