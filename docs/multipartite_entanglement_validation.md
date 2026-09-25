# Multipartite Entanglement Validation

## Date: 2026-09-25

## Purpose

Test G=O for 4-qubit multipartite entangled states.

## Setup

Bipartition 8|2 (first 3 qubits vs last qubit).

## Results

| State | G | Diff |
|-------|---|------|
| GHZ₄ | 0.5000 | 1.11e-16 |
| W₄ | 0.4330 | 1.11e-16 |
| Cluster₄ | 0.5000 | 3.33e-16 |

## Observations

1. **GHZ and Cluster states have G=0.5**
   - Maximal bipartite entanglement for this partition

2. **W state has G≈0.433**
   - Less bipartite entanglement than GHZ

3. **G=O holds for all multipartite states**

## Conclusion

G=O applies to multipartite entangled states. The equality correctly
quantifies bipartite entanglement across different partitions.
