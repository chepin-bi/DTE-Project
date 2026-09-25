# Literature Review: Negativity, Mutual Information, and Werner States

## Key Findings from Web Search

### 1. Negativity-Mutual Information Relation

From arXiv:2203.17254 (Entanglement Negativity and Mutual Information after a Quantum Quench):
- For pure states: negativity and mutual information are trivially related
- For mixed states: the relation is highly non-trivial
- The paper establishes: 2ℰ(t) = I^{(1/2)}_{A:B}(t) (exact universal relation for local quantum circuits)

This is consistent with our DTE framework's Theorem 1 (G=O) and suggests deeper
connections between entanglement measures and information-theoretic quantities.

### 2. Werner State Entanglement

From arXiv:1708.03109 (Verifying bound entanglement of dephased Werner states):
- Werner states are fundamental for testing entanglement criteria
- NPT criterion serves as reference for bound entanglement
- Qutrit Werner states show regions of bound entanglement

From Tel-Aviv University QLib:
- Werner states: ρ(x) = x|Ψ⁺⟩⟨Ψ⁺| + (1-x)I/d²
- Standard measures: negativity, concurrence, von Neumann entropy, mutual information
- All can be computed analytically for Werner states

### 3. Mutual Information Bounds

From MDPI Entropy 2022 (Estimating Quantum Mutual Information):
- CV Werner state: I(ρ) bounds derived
- For pure states: ratio I⁻(ρ)/I(ρ) ≈ 0.905 at f=1
- For mixed states: bounds become less tight

### 4. Monogamy and Multi-Party Entanglement

From PMC7841181 (Entanglement of formation and monogamy):
- GHZ state satisfies monogamy inequality: Ef(ρ_A(BC)) ≥ Ef(ρ_AB) + Ef(ρ_AC)
- W state VIOLATES monogamy inequality
- Additivity of mutual information for ccq states guarantees monogamy

This is directly relevant to our CONJ-03 (LOCC monotonicity) and multi-party extensions.

### 5. Holographic Entanglement

From arXiv:1909.13347:
- Monogamy of mutual information: S(AB) + S(AC) + S(BC) ≥ S(A) + S(B) + S(C) + S(ABC)
- Negativity has been geometrized in holography
- Connections between entanglement measures and geometry

## Implications for DTE Framework

1. **Theorem 1 (G=O)**: The exact relation between negativity and Rényi-1/2 mutual
   information in local quantum circuits supports our G=O exact equality.

2. **Theorem 2 (I ≥ c(d)·G²)**: The Werner state analysis in literature confirms
   that I and G are intimately related, but the exact constant c(d) = 8·log₂(d)/(d-1)²
   appears to be a novel result of our framework.

3. **Multi-party**: The monogamy results for GHZ vs W states suggest that our
   CONJ-01 (multi-party G=O) may hold specifically for GHZ-class states but not
   universally for all multi-party states.

4. **Next steps**: Investigate whether the I/G² ratio for W states (which violate
   monogamy) differs from GHZ states, potentially providing a classification criterion.

## References

1. arXiv:2203.17254 — Entanglement Negativity and Mutual Information after a Quantum Quench
2. arXiv:1708.03109 — Verifying bound entanglement of dephased Werner states
3. PMC7841181 — Entanglement of formation and monogamy of multi-party quantum entanglement
4. arXiv:1909.13347 — Holographic entanglement entropy
5. MDPI Entropy 2022 — Estimating Quantum Mutual Information of Continuous-Variable Quantum States
