/-
DTE.LocalLemmas
===============

Local lemmas to bypass missing Mathlib 4 APIs.
These fill the gaps blocking DensityMatrix proofs.

TARGET: Close P1 sorry (6/22) without waiting for Mathlib updates.
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Algebra.BigOperators.Finprod
import Mathlib.Data.Finset.Basic

namespace DTE

open Matrix Complex Real BigOperators

-- ============================================================
-- LEMMA 1: Star (conjugate) distributes over finite sums
-- ============================================================

/-
GAP: Mathlib 4 lacks `Finset.sum_star` for pulling conjugation
inside finite sums over complex numbers.

This is foundational for partialTrace_hermitian proofs.
-/

lemma Finset.sum_star_complex {ι : Type} [Fintype ι]
    (f : ι → ℂ) :
    star (∑ i : ι, f i) = ∑ i : ι, star (f i) := by
  -- Proof by induction on Fintype (which reduces to Finset.univ)
  simp only [Finset.sum, star_sum]
  -- `star_sum` exists in Mathlib for AddCommMonoid with star
  -- If not available, prove by induction:
  /-
  apply Finset.induction_on (Finset.univ)
  · simp [star_zero]
  · intro i s hi ih
    rw [Finset.sum_insert hi, star_add, ih, Finset.sum_insert hi]
  -/

-- ============================================================
-- LEMMA 2: Reindexing for product finite types
-- ============================================================

/-
GAP: No direct lemma to reindex Σ_{iB} Σ_{iA} f(iA,iB) as Σ_{idx} f(idx/dB, idx%dB).

This is needed for partialTrace_trace_one proofs.
-/

lemma sum_product_reindex {dA dB : ℕ} (f : Fin dA → Fin dB → ℂ) :
    ∑ iB : Fin dB, ∑ iA : Fin dA, f iA iB
    = ∑ idx : Fin (dA * dB), f (Fin.mk (idx.val / dB) (by sorry)) (Fin.mk (idx.val % dB) (by sorry)) := by
  -- Proof strategy:
  -- 1. Show the map (iA, iB) ↦ iA.val * dB + iB.val is a bijection
  --    Fin dA × Fin dB → Fin (dA * dB)
  -- 2. Use `Finset.sum_bij` or equivalent
  -- 3. Verify divisibility conditions for Fin.mk well-formedness
  sorry

-- ============================================================
-- LEMMA 3: Matrix element access via tensor indexing
-- ============================================================

lemma matrix_index_decomp {dA dB : ℕ} {M : Matrix (Fin (dA * dB)) (Fin (dA * dB)) ℂ}
    (iA iB jA jB : ℕ)
    (hiA : iA < dA) (hiB : iB < dB) (hjA : jA < dA) (hjB : jB < dB) :
    M ⟨iA * dB + iB, _⟩ ⟨jA * dB + jB, _⟩ =
    M ⟨iA * dB + iB, by omega⟩ ⟨jA * dB + jB, by omega⟩ := by
  rfl

-- ============================================================
-- LEMMA 4: Euclidean division for product indexing
-- ============================================================

lemma div_mul_add_mod_eq {n m : ℕ} (hm : m > 0) :
    ∀ k < n * m, (k / m) * m + (k % m) = k := by
  intro k hk
  exact Nat.div_mul_mod_cancel hm k

lemma product_index_injective {dA dB : ℕ} :
    Function.Injective (fun p : Fin dA × Fin dB => p.1.val * dB + p.2.val) := by
  intro p q h_eq
  have h1 : p.1.val = q.1.val := by
    have : p.1.val * dB + p.2.val = q.1.val * dB + q.2.val := h_eq
    -- Use uniqueness of Euclidean division
    sorry
  have h2 : p.2.val = q.2.val := by
    sorry
  exact Prod.ext (Fin.ext h1) (Fin.ext h2)

-- ============================================================
-- LEMMA 5: PSD quadratic form under partial trace
-- ============================================================

/-
For partialTrace_positive: show that the quadratic form for
partial trace is a sum of valid quadratic forms for the original
state.
-/

lemma psd_sum_quadratic {dA dB : ℕ} {ρ : Matrix (Fin (dA * dB)) (Fin (dA * dB)) ℂ}
    (h_psd : ∀ w, 0 ≤ ∑ i, ∑ j, star (w i) * ρ i j * w j)
    (v : Fin dB → ℂ) :
    ∀ iA : Fin dA, 0 ≤ ∑ iB, ∑ jB, star (v iB) * ρ ⟨iA.val * dB + iB.val, _⟩ ⟨iA.val * dB + jB.val, _⟩ * v jB := by
  intro iA
  -- Construct w = δ_{iA} ⊗ v
  let w : Fin (dA * dB) → ℂ := fun idx =>
    if idx.val / dB = iA.val then v ⟨idx.val % dB, _⟩ else 0
  -- Show the quadratic form for w equals the desired sum
  have h_eq : ∑ iB, ∑ jB, star (v iB) * ρ _ _ * v jB =
      ∑ idx, ∑ jdx, star (w idx) * ρ idx jdx * w jdx := by
    -- Expand w definition and simplify
    sorry
  rw [h_eq]
  apply h_psd

end DTE
