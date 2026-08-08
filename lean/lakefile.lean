import Lake
open Lake DSL

package «DTE» where
  -- add package configuration options here

lean_lib «DTE» where
  -- add library configuration options here

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

require quantumInfo from git
  "https://github.com/Timeroot/Lean-QuantumInfo.git"

@[default_target]
lean_exe «dte» where
  root := `DTE.Core
