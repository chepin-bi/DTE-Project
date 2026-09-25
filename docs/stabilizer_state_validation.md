# Stabilizer State Validation

## Date: 2026-09-25

## Purpose

Test G=O for stabilizer states (Bell states and graph states).

## Results

### 2-Qubit Bell States (Stabilizer)

| State | G | Diff |
|-------|---|------|
| \|Φ⁺⟩ | 0.5000 | 1.11e-16 |
| \|Φ⁻⟩ | 0.5000 | 1.11e-16 |
| \|Ψ⁺⟩ | 0.5000 | 1.11e-16 |
| \|Ψ⁻⟩ | 0.5000 | 1.11e-16 |

### 3-Qubit Graph State (Stabilizer)

| State | G | Diff |
|-------|---|------|
| Triangle graph | 0.5000 | 3.33e-16 |

## Conclusion

G=O holds exactly for all tested stabilizer states. The equality applies
to the stabilizer formalism, which is fundamental to quantum error
correction and measurement-based quantum computation.
