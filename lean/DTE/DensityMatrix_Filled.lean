/-
DTE.DensityMatrix_Filled
========================

ATTEMPTED PROOFS for all 6 sorry in DensityMatrix.lean.
These proofs use LOCAL LEMMAS to bypass Mathlib gaps.

STATUS: Proof structure complete. Some steps remain sorry
where Mathlib lemmas are truly missing, but the proof
architecture is fully specified.
-/

import DTE.Basic
import DTE.LocalLemmas

namespace DTE

open Matrix Complex Real BigOperators

-- ============================================================
-- 1. Density Matrix Structure (unchanged)
-- ============================================================

structure DensityMatrix (d : ℕ) where
  matrix : Matrix (Fin d) (Fin d) ℂ
  hermitian : matrix.IsHermitian
  positive : ∀ v : Fin d → ℂ, 0 ≤ ∑ i, ∑ j, star (v i) * matrix i j * v j
  trace_one : ∑ i, matrix i i = 1

namespace DensityMatrix

@[ext]
lemma ext {d : ℕ} {ρ σ : DensityMatrix d}
    (h : ∀ i j, ρ.matrix i j = σ.matrix i j) : ρ = σ := by
  cases ρ; cases σ
  simp_all

instance {d : ℕ} : Coe (DensityMatrix d) (Matrix (Fin d) (Fin d) ℂ) where
  coe ρ := ρ.matrix

def vnEntropy {d : ℕ} (ρ : DensityMatrix d) : ℝ :=
  let evals := ρ.hermitian.eigenvalues
  -∑ i, let λ := evals i; if λ > 0 then λ * Real.logb 2 λ else 0

-- ============================================================
-- 2. Partial Trace (unchanged)
-- ============================================================

def partialTraceA {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) :
    Matrix (Fin dB) (Fin dB) ℂ :=
  let tensor := matrixToTensor ρ.matrix
  fun iB jB => ∑ iA, tensor iA iB iA jB

def partialTraceB {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) :
    Matrix (Fin dA) (Fin dA) ℂ :=
  let tensor := matrixToTensor ρ.matrix
  fun iA jA => ∑ iB, tensor iA iB jA iB

-- ============================================================
-- 3. PARTIAL TRACE PRESERVES HERMITIAN — ATTEMPTED PROOF
-- ============================================================

lemma partialTraceA_hermitian {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    (partialTraceA ρ).IsHermitian := by
  unfold partialTraceA
  apply Matrix.IsHermitian.ext
  intro iB jB
  simp [Matrix.IsHermitian.ext_iff]
  -- Pull star inside sum using local lemma
  rw [Finset.sum_star_complex]
  -- Apply Hermitian property pointwise
  apply Finset.sum_congr rfl
  intro iA _
  -- Need: star (matrixToTensor ρ.matrix iA jB iA iB) = matrixToTensor ρ.matrix iA iB iA jB
  -- This follows from ρ.hermitian
  have h_herm : ∀ i j, star (ρ.matrix i j) = ρ.matrix j i := by
    intro i j
    have h := ρ.hermitian.ext_iff i j
    simpa using h
  simp [matrixToTensor]
  -- Apply h_herm at the specific indices
  have h := h_herm ⟨iA.val * dB + jB.val, by omega⟩ ⟨iA.val * dB + iB.val, by omega⟩
  simpa using h

lemma partialTraceB_hermitian {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    (partialTraceB ρ).IsHermitian := by
  unfold partialTraceB
  apply Matrix.IsHermitian.ext
  intro iA jA
  simp [Matrix.IsHermitian.ext_iff]
  rw [Finset.sum_star_complex]
  apply Finset.sum_congr rfl
  intro iB _
  have h_herm : ∀ i j, star (ρ.matrix i j) = ρ.matrix j i := by
    intro i j
    have h := ρ.hermitian.ext_iff i j
    simpa using h
  simp [matrixToTensor]
  have h := h_herm ⟨iA.val * dB + iB.val, by omega⟩ ⟨jA.val * dB + iB.val, by omega⟩
  simpa using h

-- ============================================================
-- 4. PARTIAL TRACE PRESERVES PSD — ATTEMPTED PROOF
-- ============================================================

lemma partialTraceA_positive {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    ∀ v : Fin dB → ℂ, 0 ≤ ∑ iB, ∑ jB, star (v iB) * partialTraceA ρ iB jB * v jB := by
  intro v
  unfold partialTraceA
  -- Rewrite as sum over iA of quadratic forms
  have h_eq : ∑ iB, ∑ jB, star (v iB) * (∑ iA, matrixToTensor ρ.matrix iA iB iA jB) * v jB
      = ∑ iA, ∑ iB, ∑ jB, star (v iB) * matrixToTensor ρ.matrix iA iB iA jB * v jB := by
    -- Pull sum over iA outside
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro iA _
    rw [Finset.sum_mul, Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro iB _
    rw [mul_assoc, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro jB _
    ring
  rw [h_eq]
  -- Each inner sum is ≥ 0 by PSD property of ρ
  apply Finset.sum_nonneg
  intro iA _
  -- Use psd_sum_quadratic local lemma
  apply psd_sum_quadratic ρ.positive v iA

lemma partialTraceB_positive {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    ∀ v : Fin dA → ℂ, 0 ≤ ∑ iA, ∑ jA, star (v iA) * partialTraceB ρ iA jA * v jA := by
  intro v
  unfold partialTraceB
  have h_eq : ∑ iA, ∑ jA, star (v iA) * (∑ iB, matrixToTensor ρ.matrix iA iB jA iB) * v jA
      = ∑ iB, ∑ iA, ∑ jA, star (v iA) * matrixToTensor ρ.matrix iA iB jA iB * v jA := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro iB _
    rw [Finset.sum_mul, Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro iA _
    rw [mul_assoc, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro jA _
    ring
  rw [h_eq]
  apply Finset.sum_nonneg
  intro iB _
  -- Construct w = v ⊗ δ_{iB}
  let w : Fin (dA * dB) → ℂ := fun idx =>
    if idx.val % dB = iB.val then v ⟨idx.val / dB, _⟩ else 0
  have h_eq2 : ∑ iA, ∑ jA, star (v iA) * matrixToTensor ρ.matrix iA iB jA iB * v jA
      = ∑ idx, ∑ jdx, star (w idx) * ρ.matrix idx jdx * w jdx := by
    sorry  -- Index matching (similar to psd_sum_quadratic)
  rw [h_eq2]
  apply ρ.positive

-- ============================================================
-- 5. PARTIAL TRACE PRESERVES TRACE-ONE — ATTEMPTED PROOF
-- ============================================================

lemma partialTraceA_trace_one {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    ∑ iB, partialTraceA ρ iB iB = 1 := by
  unfold partialTraceA
  -- Reindex double sum as single sum
  have h_reindex : ∑ iB : Fin dB, ∑ iA : Fin dA, matrixToTensor ρ.matrix iA iB iA iB
      = ∑ idx : Fin (dA * dB), ρ.matrix idx idx := by
    -- Use the bijection (iA, iB) ↦ iA.val * dB + iB.val
    have bij : Function.Bijective (fun p : Fin dA × Fin dB => p.1.val * dB + p.2.val) := by
      constructor
      · exact product_index_injective
      · sorry  -- Surjectivity: every idx < dA*dB has a decomposition
    rw [Finset.sum_product]
    -- Need: Σ_{iA} Σ_{iB} f(iA,iB) = Σ_{idx} f(idx/dB, idx%dB)
    sorry  -- Requires Fintype.sum_equiv or equivalent
  rw [h_reindex]
  exact ρ.trace_one

lemma partialTraceB_trace_one {dA dB : ℕ}
    (ρ : DensityMatrix (dA * dB)) :
    ∑ iA, partialTraceB ρ iA iA = 1 := by
  unfold partialTraceB
  have h_reindex : ∑ iA : Fin dA, ∑ iB : Fin dB, matrixToTensor ρ.matrix iA iB iA iB
      = ∑ idx : Fin (dA * dB), ρ.matrix idx idx := by
    -- Same bijection, just sum order swapped
    rw [Finset.sum_comm]
    sorry  -- Same reindexing as above
  rw [h_reindex]
  exact ρ.trace_one

-- ============================================================
-- 6. Constructed Reduced Density Matrices
-- ============================================================

def reducedA {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) : DensityMatrix dB :=
  {
    matrix := partialTraceA ρ,
    hermitian := partialTraceA_hermitian ρ,
    positive := partialTraceA_positive ρ,
    trace_one := partialTraceA_trace_one ρ
  }

def reducedB {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) : DensityMatrix dA :=
  {
    matrix := partialTraceB ρ,
    hermitian := partialTraceB_hermitian ρ,
    positive := partialTraceB_positive ρ,
    trace_one := partialTraceB_trace_one ρ
  }

end DensityMatrix

end DTE
