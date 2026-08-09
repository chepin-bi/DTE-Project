# DTE Lean 4 Formalization

## Overview

This directory contains the Lean 4 formalization of the DTE (Derived Triangle Equivalence) framework. The formalization covers:

- **Density matrices** with Hermitian, positive semidefinite, and trace-one properties
- **Partial transpose** operation for bipartite systems
- **Negativity** and **Boundary Obstruction** (G and O faces)
- **von Neumann entropy** and **mutual information** (I face)
- **Theorem 1**: G = O exactly for all dimensions
- **Theorem 2**: I ≥ c(d)·G² for pure states
- **Theorem 3**: Low-dimensional equivalence (G=0 ⟺ separable for 2×2, 2×3)
- **Theorem 4**: Existence of PPT-bound entangled states for d ≥ 3

## Prerequisites

Install Lean 4 via [elan](https://github.com/leanprover/elan):

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

## Build

```bash
cd lean
lake update       # Download dependencies (mathlib4)
lake build        # Compile the project
```

## Structure

```
lean/
├── DTE/
│   ├── Basic.lean           -- Type aliases, utilities, eigenvalue helpers
│   ├── DensityMatrix.lean   -- Density matrix structure, partial traces
│   ├── PartialTranspose.lean -- Partial transpose, Hermitian/trace preservation
│   ├── Negativity.lean      -- G=O definitions, Theorem 1
│   ├── Entropy.lean         -- von Neumann entropy, mutual information (I face)
│   ├── Theorem2.lean        -- Information-geometric inequality
│   ├── Classification.lean  -- Entanglement types, Theorems 3 and 4
│   └── Core.lean            -- Main entry point, re-exports
├── lakefile.lean            -- Project configuration
├── lean-toolchain           -- Lean version (v4.15.0)
└── README.md                -- This file
```

## Module Dependencies

```
Basic
  ↓
DensityMatrix ← Basic
  ↓
PartialTranspose ← Basic + DensityMatrix
  ↓
Negativity ← Basic + DensityMatrix + PartialTranspose
  ↓
Entropy ← Basic + DensityMatrix
  ↓
Theorem2 ← Basic + DensityMatrix + Negativity + Entropy
  ↓
Classification ← Basic + DensityMatrix + Negativity + Entropy
  ↓
Core ← All modules
```

## Theorem Status

| Theorem | Statement | Status |
|---------|-----------|--------|
| Theorem 1 | G(ρ) = O(ρ) exactly | Framework complete, proofs as `sorry` |
| Theorem 2 | I(ρ) ≥ c(d)·G(ρ)² | Framework complete, d=2 special case outlined |
| Theorem 3 | G=0 ⟺ separable (2×2, 2×3) | Uses Horodecki as axiom |
| Theorem 4 | PPT-bound entangled exists (d≥3) | Existence stated, construction as `sorry` |

## Contributing

To fill in a `sorry`:

1. Locate the theorem in the corresponding `.lean` file
2. Replace `sorry` with a proof using Mathlib 4 tactics
3. Run `lake build` to verify
4. Submit a PR

## Integration with Mathlib 4

This project depends on Mathlib 4 (v4.15.0) for:
- Matrix operations (`Mathlib.Data.Matrix`)
- Hermitian matrices (`Mathlib.LinearAlgebra.Matrix.Hermitian`)
- Spectral theory (`Mathlib.LinearAlgebra.Matrix.Spectrum`)
- Real analysis (`Mathlib.Analysis.SpecialFunctions.Log`)

## References

1. Horodecki et al. (1996) -- PPT criterion
2. Vidal & Werner (2002) -- Negativity measure
3. Ryu & Takayanagi (2006) -- Holographic entanglement entropy
4. Meiburg (2024) -- Lean-QuantumInfo library
