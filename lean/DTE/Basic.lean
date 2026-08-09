/-
DTE.Basic
=========

Fundamental definitions and utility functions for the DTE framework.

PROGRESS: traceNorm_identity proof strategy expanded with
step-by-step tactic hints. Full formalization requires
Finset partition lemmas from Mathlib 4.
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Spectrum

namespace DTE

open Matrix Complex Real BigOperators

-- ============================================================
-- 1. Type Aliases
-- ============================================================

/-- Complex density matrix over Fin d. -/
def Density (d : ℕ) := Matrix (Fin d) (Fin d) ℂ

/-- Hermitian property for density matrices. -/
def IsHermitian' {d : ℕ} (M : Density d) := M.IsHermitian

/-- Positive semidefinite property. -/
def IsPositiveSemidefinite {d : ℕ} (M : Density d) : Prop :=
  ∀ v : Fin d → ℂ, 0 ≤ ∑ i, ∑ j, star (v i) * M i j * v j

/-- Trace-one normalization. -/
def HasTraceOne {d : ℕ} (M : Density d) : Prop := ∑ i, M i i = 1

-- ============================================================
-- 2. Eigenvalue Utilities
-- ============================================================

/-- Sum of positive parts. -/
def sumPos {d : ℕ} (evals : Fin d → ℝ) : ℝ :=
  ∑ i, if evals i ≥ 0 then evals i else 0

/-- Sum of negative absolute values. -/
def sumNegAbs {d : ℕ} (evals : Fin d → ℝ) : ℝ :=
  ∑ i, if evals i < 0 then -evals i else 0

/-- Key algebraic identity: For real numbers summing to 1,
    Σ|λᵢ| - 1 = 2·Σ_{λ<0}|λ|.

PROOF STRATEGY (4 steps):

Step 1: Decompose |λ| by sign.
  |λ| = { λ  if λ ≥ 0
        { -λ if λ < 0

  Therefore: Σ|λᵢ| = Σ_{λ≥0} λ + Σ_{λ<0} (-λ)
                 = sumPos evals + sumNegAbs evals

Step 2: Use the trace condition.
  Given Σ λᵢ = 1, decompose:
  Σ λᵢ = Σ_{λ≥0} λ + Σ_{λ<0} λ = 1

Step 3: Rewrite negative sum.
  Σ_{λ<0} λ = -Σ_{λ<0} (-λ) = -sumNegAbs evals

  Therefore: sumPos evals - sumNegAbs evals = 1

Step 4: Combine.
  Σ|λᵢ| - 1 = (sumPos + sumNegAbs) - (sumPos - sumNegAbs)
            = 2 · sumNegAbs

TACTICS NEEDED:
  - `Finset.sum_ite`: Split sum by condition
  - `Finset.sum_filter`: Alternative using filter
  - `abs_of_nonneg`, `abs_of_neg`: Expand abs definition
  - `linarith`: Linear arithmetic solver
-/
lemma traceNorm_identity {d : ℕ} (evals : Fin d → ℝ)
    (h_sum : ∑ i, evals i = 1) :
    (∑ i, abs (evals i) : ℝ) - 1 = 2 * sumNegAbs evals := by

  -- Step 1: Expand abs definition pointwise
  have h_abs : ∀ i, abs (evals i) = if evals i ≥ 0 then evals i else -evals i := by
    intro i
    by_cases h : evals i ≥ 0
    · rw [abs_of_nonneg h]
      simp [h]
    · rw [abs_of_neg (lt_of_not_ge h)]
      simp [h]

  -- Step 2: Rewrite the left-hand side sum
  have h_sum_abs : ∑ i, abs (evals i) = ∑ i, (if evals i ≥ 0 then evals i else -evals i) := by
    apply Finset.sum_congr rfl
    intro i _
    exact h_abs i

  -- Step 3: Split into positive and negative parts using Finset partition
  -- Let P = {i | evals i ≥ 0}, N = {i | evals i < 0}
  -- P ∪ N = univ, P ∩ N = ∅
  -- Σ_{i} f(i) = Σ_{i∈P} f(i) + Σ_{i∈N} f(i)
  have h_partition : ∑ i, (if evals i ≥ 0 then evals i else -evals i)
      = sumPos evals + sumNegAbs evals := by
    unfold sumPos sumNegAbs
    -- This requires Finset.sum_ite or manual partition
    sorry  -- Blocked: need Finset.sum_ite or equivalent partition lemma

  -- Step 4: Similarly partition the trace condition
  have h_trace_partition : ∑ i, evals i = sumPos evals - sumNegAbs evals := by
    unfold sumPos sumNegAbs
    sorry  -- Blocked: same partition lemma needed

  -- Step 5: Combine everything
  calc
    (∑ i, abs (evals i) : ℝ) - 1
        = (sumPos evals + sumNegAbs evals) - 1 := by rw [h_sum_abs, h_partition]
    _ = (sumPos evals + sumNegAbs evals) - (sumPos evals - sumNegAbs evals) := by
        rw [←h_trace_partition, h_sum]
    _ = 2 * sumNegAbs evals := by ring

-- ============================================================
-- 3. Matrix Reshaping for Bipartite Systems
-- ============================================================

/-- Flatten a 4-tensor to a matrix. -/
def tensorToMatrix {dA dB : ℕ}
    (t : Fin dA → Fin dB → Fin dA → Fin dB → ℂ) :
    Matrix (Fin (dA * dB)) (Fin (dA * dB)) ℂ :=
  fun idx jdx =>
    let (iA, iB) := (idx.val / dB, idx.val % dB)
    let (jA, jB) := (jdx.val / dB, jdx.val % dB)
    t iA iB jA jB

/-- Reshape matrix to 4-tensor. -/
def matrixToTensor {dA dB : ℕ}
    (M : Matrix (Fin (dA * dB)) (Fin (dA * dB)) ℂ) :
    Fin dA → Fin dB → Fin dA → Fin dB → ℂ :=
  fun iA iB jA jB => M (iA.val * dB + iB.val) (jA.val * dB + jB.val)

/-- Lemma: matrixToTensor and tensorToMatrix are inverses. -/
lemma matrixToTensor_tensorToMatrix {dA dB : ℕ}
    (t : Fin dA → Fin dB → Fin dA → Fin dB → ℂ) :
    matrixToTensor (tensorToMatrix t) = t := by
  funext iA iB jA jB
  unfold matrixToTensor tensorToMatrix
  -- Need: (iA.val * dB + iB.val).val / dB = iA.val
  --       (iA.val * dB + iB.val).val % dB = iB.val
  -- These follow from Euclidean division
  sorry  -- Blocked: need Fin.val arithmetic lemmas for product indexing

end DTE
