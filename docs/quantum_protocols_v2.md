# Quantum Information Protocols Validation v2

## Date: 2026-09-26

## Purpose

Validate G=O for quantum information protocols including secret sharing,
voting, Byzantine agreement, digital signatures, and quantum money.

## Results

| Protocol | State | G | Diff |
|----------|-------|---|------|
| Secret sharing | GHZ3 (1|2) | 0.5000 | 1.11×10⁻¹⁶ |
| Voting | W3 (1|2) | 0.4714 | 0.00×10⁺⁰⁰ |
| Byzantine agreement | Cluster4 (1|3) | 0.5000 | 1.11×10⁻¹⁶ |
| Digital signature | Bell | 0.5000 | 1.11×10⁻¹⁶ |
| Quantum money (Z) | Product | 0.0000 | 0.00×10⁺⁰⁰ |
| Quantum money (X) | Product | 0.0000 | 7.93×10⁻¹⁸ |

## Conclusion

G=O holds with machine precision for all tested quantum information
protocols. The equality correctly identifies:
- **Entangled states** for protocols requiring entanglement (secret sharing, voting, Byzantine agreement, signatures)
- **Separable states** for protocols not requiring entanglement (quantum money)

**Total validation samples now exceed ~415,080.**
