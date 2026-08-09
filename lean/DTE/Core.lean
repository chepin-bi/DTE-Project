/-
DTE.Core
========

Main entry point for the DTE Lean 4 formalization.
Re-exports all modules and provides convenient access to core theorems.
-/

import DTE.Basic
import DTE.DensityMatrix
import DTE.PartialTranspose
import DTE.Negativity
import DTE.Entropy
import DTE.Theorem2
import DTE.Classification

namespace DTE

/-- Convenient re-export of the DTE triple. -/
structure Triple {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) where
  G : ℝ := negativity ρ
  I : ℝ := mutualInformation ρ
  O : ℝ := boundaryObstruction ρ

/-- DTE triple satisfies G = O (Theorem 1). -/
theorem Triple.G_eq_O {dA dB : ℕ} {ρ : DensityMatrix (dA * dB)} :
    (Triple ρ).G = (Triple ρ).O := by
  exact theorem1_G_eq_O ρ

/-- The complete DTE framework in one line. -/
def DTE fingerprint {dA dB : ℕ} (ρ : DensityMatrix (dA * dB)) :
    ℝ × ℝ × ℝ × EntanglementType :=
  let t := Triple ρ
  let cls := classify ρ
  (t.G, t.I, t.O, cls)

end DTE
