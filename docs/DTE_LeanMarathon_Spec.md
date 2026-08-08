# DTE-Marathon Project Specification
## For LeanMarathon Automatic Formalization

---

### Project Name
**DTE-SIUπ-AX Core Framework**

### Description
Formalize the Derived Triangle Equivalence (DTE) unified framework
in Lean 4, proving the four main theorems of the DTE-Generalized conjecture.

### Budget
$257 (standard LeanMarathon project fee)

---

### Deliverables

#### Module 1: Quantum Information Foundations (Week 1-2)
- [ ] DensityMatrix structure (positive, Hermitian, trace-1)
- [ ] Partial transpose operation
- [ ] von Neumann entropy
- [ ] Trace norm and Schatten norms

#### Module 2: DTE Triple Invariant (Week 2-3)
- [ ] G(ρ) = Negativity = (||ρ^T_A||_1 - 1)/2
- [ ] I(ρ) = Mutual Information = S(ρ_A) + S(ρ_B) - S(ρ)
- [ ] O(ρ) = Boundary Obstruction = Σ_{λ<0} |λ|

#### Module 3: Core Theorems (Week 3-5)
- [ ] **Theorem 1**: G(ρ) = O(ρ) for all dimensions (EXACT EQUALITY)
- [ ] **Theorem 2**: I(ρ) ≥ c(d)·G(ρ)² with c(d) = 8log₂d/(d-1)²
- [ ] **Theorem 3**: Low-dimensional equivalence (2×2, 2×3 systems)
- [ ] **Theorem 4**: High-dimensional splitting (PPT-Bound Entanglement)

#### Module 4: Classification (Week 5-6)
- [ ] EntanglementType inductive type
- [ ] classify function
- [ ] Properties of each class

#### Module 5: Cross-Paradigm Bridge (Week 6-8)
- [ ] Atiyah-Singer ↔ DTE correspondence
- [ ] Mirror Symmetry ↔ DTE correspondence
- [ ] Langlands ↔ DTE correspondence (function field)
- [ ] Factorization Homology ↔ DTE correspondence

---

### Theorem Dependencies

```
Lemma 1.1 (Trace Norm-Negative Eigenvalues)
    └── Theorem 1 (G = O)
        ├── Theorem 3 (Low-dim equivalence)
        │   └── Horodecki PPT Theorem
        └── Theorem 4 (High-dim splitting)
            └── Horodecki Construction
                └── Brandão-Christandl-Yard

Lemma 2.1 (Entropy-Quadratic Inequality)
    └── Theorem 2 (I ≥ c·G²)
        └── Numerical verification for d=2,3,4
```

---

### Key Lemmas Needed from Mathlib

| Lemma | Mathlib Location | Status |
|-------|-------------------|--------|
| Hermitian eigenvalues real | `Matrix.IsHermitian.eigenvalues` | ✅ |
| Trace = sum of eigenvalues | `Matrix.trace_eq_sum_eigenvalues` | ✅ |
| Partial transpose preserves Hermitian | Need proof | ⚠️ |
| von Neumann entropy definition | Need definition | ⚠️ |
| Trace norm definition | Need definition | ⚠️ |
| PPT criterion equivalence | Need proof (2×2, 2×3) | ⚠️ |

---

### Expected Output

1. `DTE/Core.lean` - Core definitions
2. `DTE/Quantum.lean` - Quantum information utilities
3. `DTE/Theorem1.lean` - G = O proof
4. `DTE/Theorem2.lean` - I ≥ c·G² proof
5. `DTE/Theorem3.lean` - Low-dim equivalence
6. `DTE/Theorem4.lean` - High-dim splitting
7. `DTE/Classification.lean` - Entanglement classifier
8. `DTE/Paradigms.lean` - Cross-paradigm bridges

---

### Success Criteria

- [ ] All 4 theorems compile in Lean 4
- [ ] No `sorry` tactics remaining
- [ ] CI passes on GitHub Actions
- [ ] Documentation complete
- [ ] Benchmark: verification on 100 random states < 1s

---

### Contact
Email: chepin@163.com
GitHub: (via GitHub API token)
