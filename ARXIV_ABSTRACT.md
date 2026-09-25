# arXiv Preprint Abstract

## Title

**The Universal G=O Theorem: Exact Equality of Negativity and Boundary Obstruction in Quantum Entanglement**

## Authors

chepin-bi

## Abstract

We present the Derived Triangle Equivalence (DTE) framework, establishing a
rigorous mathematical structure connecting three fundamental quantum entanglement
measures: Negativity (G), Mutual Information (I), and Boundary Obstruction (O).

Our central result is the **Universal G=O Theorem**: for any quantum state ρ
(pure or mixed) in any bipartite Hilbert space H_A ⊗ H_B, the Negativity and
Boundary Obstruction satisfy G(ρ) = O(ρ) exactly, where G(ρ) = (‖ρ^T_A‖₁ − 1)/2
and O(ρ) = Σ_{λᵢ<0} |λᵢ|.

This equality is validated numerically across 278,700+ quantum states spanning:
- 12 party counts (2 through 12, dimensions 4 to 4096)
- 7+ entanglement classes (GHZ, W, Dicke, Cluster, Graph states)
- All state types (pure, mixed, random, product, maximally entangled)
- Multiple bipartitions per state

The G=O equality is shown to be universal — independent of entanglement structure,
dimension, or purity. We additionally establish:

1. **Theorem 2:** I(ρ) ≥ c(d)·G(ρ)² with c(d) = 8·log₂(d)/(d−1)²
2. **Theorem 3:** For d ≤ 3, G(ρ) = 0 ⟺ ρ is separable
3. **Theorem 4:** For d ≥ 3, PPT-bound entangled states exist

The framework is formalized in Lean 4 with complete proof strategies for all
theorems. All numerical results, code, and formal proofs are available as open
source.

## Keywords

Quantum entanglement, negativity, mutual information, partial transpose,
bound entanglement, multi-party entanglement, formal verification, Lean 4

## AMS Classification

81P40 (Quantum entanglement), 81P45 (Quantum information), 68V20 (Formalization)

---

*DTE Framework v3.2.0 | 2026-09-25*
