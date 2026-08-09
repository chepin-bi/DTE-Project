# DTE Technical Debt & Open Problems Tracker

## Overview

This document tracks all technical debt, open problems, and future directions for the DTE (Derived Triangle Equivalence) framework. It serves as the single source of truth for what remains incomplete and what needs community contribution.

**Last Updated:** 2025-01-10
**Version:** 3.0.0-P3
**GitHub:** https://github.com/chepin-ai/DTE-Project

---

## 1. Lean 4 Formalization Debt

### 1.1 Theorem 1: G = O (Exact Equality)

**Status:** Framework complete, 3 `sorry` remaining
**Priority:** High
**Location:** `lean/DTE/Negativity.lean`

**Remaining Proof Steps:**

| Step | Description | Mathlib 4 Need |
|------|-------------|----------------|
| 1 | `traceNorm_identity` sum splitting | `Finset.filter`, `Finset.sum_ite` |
| 2 | Trace equals sum of eigenvalues | `Matrix.trace_eq_sum_eigenvalues` |
| 3 | Max(0, ...) wrapper handling | `Real.max_eq_left` with positivity proof |

**Proof Strategy:**
```
1. Partition eigenvalues into {λ ≥ 0} and {λ < 0}
2. Use Σ|λ| = Σ_{λ≥0} λ + Σ_{λ<0}(-λ)
3. Use Tr(ρ) = Σ λ = 1
4. Show Σ|λ| - 1 = 2·Σ_{λ<0}|λ|
```

**Community Action:** Fill in `traceNorm_boundaryObstruction` lemma using `Finset` partition tactics.

---

### 1.2 Theorem 2: I ≥ c(d)·G²

**Status:** Framework complete, 3 `sorry` remaining
**Priority:** High
**Location:** `lean/DTE/Theorem2.lean`

**Remaining Proof Steps:**

| Step | Description | Approach |
|------|-------------|----------|
| 1 | Schmidt decomposition for pure states | `Matrix.spectral_theorem` + `tensor_product` |
| 2 | Express G in Schmidt coefficients | Closed form for pure state negativity |
| 3 | Convexity/optimization argument | `Real.convexOn` + `Lagrange_multipliers` |

**d=2 Special Case:** `h₂(p) ≥ 4p(1-p)` — numerically verified, needs formal convexity proof.

**Community Action:** Use `Mathlib.Analysis.Convex` for the optimization step.

---

### 1.3 Theorem 3: Low-Dimensional Equivalence

**Status:** Framework complete, 3 `sorry` remaining
**Priority:** Medium
**Location:** `lean/DTE/Classification.lean`

**Key Blocker:** Need proof that separable states have I = 0.

**Remaining Proof Steps:**
- Separable states have I = 0 (convexity of entropy)
- PPT criterion equivalence with G = 0 (by definition)
- Horodecki theorem stated as `axiom` (valid — this is a major theorem)

**Community Action:** Prove `separable_states_I_zero` using `von_Neumann_entropy_convex`.

---

### 1.4 Theorem 4: PPT-Bound Existence

**Status:** Framework complete, 1 `sorry` remaining
**Priority:** Medium
**Location:** `lean/DTE/Classification.lean`

**Blocker:** Explicit UPB construction requires `Matrix` basis construction.

**Alternative Approach:** Instead of explicit construction, prove existence via:
1. Choi-Jamiołkowski isomorphism
2. Positive but not completely positive maps

**Community Action:** Implement `ChoiMatrix` constructor or cite UPB construction.

---

### 1.5 Partial Trace Properties

**Status:** 6 `sorry` (3 in reducedA, 3 in reducedB)
**Priority:** High
**Location:** `lean/DTE/DensityMatrix.lean`

**Needed:** Prove partial trace preserves Hermitian, PSD, and trace-1.

**Mathlib 4 Path:** `Matrix.trace_kronecker` + `IsHermitian.transpose`.

---

## 2. Python Architecture Debt

### 2.1 Package Structure

**Status:** RESOLVED ✅

- Removed `python/__init__.py` (was pointing to non-existent `.dte` module)
- Removed `setup.py` (redundant with `pyproject.toml`)
- Removed `python/dte_core.egg-info/` (build artifact, now in `.gitignore`)
- Added `requirements.txt` and `MANIFEST.in`
- Added `tests/__init__.py` and `examples/__init__.py`

### 2.2 Test Coverage

**Status:** Partially resolved

- Merged `test_dte_core.py` (v2.0, outdated) into `test_core.py` (v3.0)
- Added `TestTheorems` class with multi-dimensional tests
- Added `test_information_geometric_constant` for c(d) verification

**Remaining:**
- Add test for `examples/` usage
- Add integration test for `dte.api`
- Add benchmark regression tests

### 2.3 Module Completeness

| Module | Status | Missing |
|--------|--------|---------|
| `core` | ✅ Complete | — |
| `states` | ✅ Complete | — |
| `classification` | ✅ Complete | — |
| `io` | ✅ Complete | — |
| `viz` | ✅ Complete | — |
| `cli` | ✅ Complete | — |
| `api` | ✅ Complete | — |
| `benchmark` | ✅ Complete | — |
| `config` | ✅ Complete | — |
| `utils` | ✅ Complete | — |
| `exceptions` | ✅ Complete | — |
| `logging_config` | ✅ Complete | — |

---

## 3. Documentation Debt

### 3.1 Overlapping Documents

**Problem:** `docs/ENGINEERING_REPORT.md` and `docs/P2_Full_Spectrum_Report.md` overlap significantly.

**Resolution:** Keep both (they serve different purposes: engineering vs. research report), but add cross-references.

### 3.2 Missing Documentation

- [ ] `lean/DTE/Proofs.lean` — Centralized proof strategy document
- [ ] `docs/CONTRIBUTING.md` — Contributor guidelines for Lean 4 and Python
- [ ] API documentation (auto-generated from docstrings)
- [ ] Tutorial notebook for Jupyter

---

## 4. Open Problems & Future Directions

### 4.1 Conjectures

| # | Conjecture | Status | Priority |
|---|------------|--------|----------|
| 1 | `G = O` for all multipartite systems | Open | High |
| 2 | `I ≥ c(d)·G²` for mixed states | Open (verified numerically for many cases) | High |
| 3 | `DTE_score` is monotonic under LOCC | Open | Medium |
| 4 | `c(d)` is optimal for all d | Open (proven for d=2) | Medium |
| 5 | DTE classifies all multipartite entanglement | Conjecture | Low |

### 4.2 Future Applications

- **Quantum Gravity:** DTE in AdS/CFT (work in progress in `docs/P2_Quantum_Gravity_Coupling.md`)
- **Neuroscience:** EEG/fMRI entanglement analysis (`docs/P2_Neuroscience_Application.md`)
- **Game Theory:** Quantum game equilibria (`docs/P2_Economics_GameTheory.md`)
- **Finance:** Portfolio correlation as entanglement
- **Error Correction:** QEC code distance via DTE

### 4.3 Proposals

| Proposal | Description | Status |
|----------|-------------|--------|
| Lean 4 Proof Marathon | Fill all 18 `sorry` in 6 months | Proposed |
| DTE arXiv Paper | Combine Python numerics + Lean formalization | Proposed |
| PyPI Package | Publish `dte-core` v3.0.0 | Ready (pending tests) |
| Docker Image | Pre-built Lean + Python environment | Proposed |
| Web Interface | Interactive DTE calculator | Proposed |
| Quantum SDK Integration | Qiskit/QuTiP/Cirq native support | Partial |

---

## 5. CI/CD Debt

### 5.1 Resolved Issues

- ✅ Fixed `.github/workflows/ci.yml` to include Lean 4 build test
- ✅ Added Python 3.9-3.12 matrix
- ✅ Added flake8/black/isort/mypy lint pipeline

### 5.2 Remaining Issues

- [ ] Add `lake build` to pre-commit hooks
- [ ] Add benchmark regression CI (compare PR vs. main)
- [ ] Add Docker build verification
- [ ] Add PyPI publish workflow (on release tag)
- [ ] Add code coverage badge to README

---

## 6. Quick Reference: `sorry` Locations

```
lean/DTE/Basic.lean:            1 sorry  (traceNorm_identity)
lean/DTE/DensityMatrix.lean:    6 sorry  (3 in reducedA, 3 in reducedB)
lean/DTE/PartialTranspose.lean: 2 sorry  (Hermitian proof, PPT criterion)
lean/DTE/Negativity.lean:       3 sorry  (sum splitting, trace-eigenvalue, max)
lean/DTE/Entropy.lean:          3 sorry  (nonnegativity, product state, 3 in constructor)
lean/DTE/Theorem2.lean:         3 sorry  (Schmidt coeff, convexity, d=2 case)
lean/DTE/Classification.lean:   4 sorry  (PPT proof, separable I=0, reverse, existence)
─────────────────────────────────────────────────────────────────
Total:                          22 sorry  (down from 35 occurrences)
```

---

## 7. How to Contribute

### 7.1 Filling a `sorry`

1. Choose a `sorry` from the list above
2. Read the detailed proof strategy comment above it
3. Identify the needed Mathlib 4 lemma
4. Search [Mathlib 4 docs](https://leanprover-community.github.io/mathlib4_docs/) for the lemma
5. If lemma doesn't exist, prove it using lower-level tactics
6. Run `lake build` in `lean/` directory to verify
7. Submit a PR with `#[sorry]` in the title to track progress

### 7.2 Adding Python Features

1. Follow `black` formatting (line length 100)
2. Add tests in `tests/test_<module>.py`
3. Ensure `pytest` passes: `pytest tests/ -v`
4. Add type hints (enforced by `mypy`)
5. Update `__init__.py` exports if adding new public API

---

## 8. Contact

- Issues: https://github.com/chepin-ai/DTE-Project/issues
- Discussions: https://github.com/chepin-ai/DTE-Project/discussions
- Email: chepin@163.com
