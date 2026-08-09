/-
DTE.Basic
=========

Fundamental definitions and utility functions for the DTE framework.
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
    Σ|λᵢ| - 1 = 2·Σ_{λ<0}|λ|. -/
lemma traceNorm_identity {d : ℕ} (evals : Fin d → ℝ)
    (h_sum : ∑ i, evals i = 1) :
    (∑ i, abs (evals i) : ℝ) - 1 = 2 * sumNegAbs evals := by
  -- Proof strategy:
  -- 1. Σ|λᵢ| = Σ_{λ≥0} λ + Σ_{λ<0} (-λ)
  -- 2. 1 = Σ λ = Σ_{λ≥0} λ - Σ_{λ<0} (-λ)
  -- 3. Subtract: Σ|λᵢ| - 1 = 2·Σ_{λ<0} (-λ)
  -- This is the heart of Theorem 1.
  sorry

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

end DTE
