# Quantum Error Correction State Validation

## Date: 2026-09-25

## Purpose

Test G=O for states used in quantum error correction codes.

## Results

### 3-Qubit Bit-Flip Code

| State | Bipartition | G | Diff |
|-------|-------------|---|------|
| \|+_L⟩ | 1\|2 | 0.5000 | 1.11e-16 |

### 3-Qubit Phase-Flip Code

| State | Bipartition | G | Diff |
|-------|-------------|---|------|
| \|+_L⟩ | 1\|2 | 0.5000 | 2.78e-16 |

### Repetition Codes

| n | Bipartition | G | Diff |
|---|-------------|---|------|
| 3 | 1\|2 | 0.5000 | 1.11e-16 |
| 4 | 1\|3 | 0.5000 | 1.11e-16 |
| 5 | 1\|4 | 0.5000 | 1.11e-16 |

## Observations

1. **All logical |+_L⟩ states have G=0.5**
   - These are GHZ-type states (cat states in logical basis)

2. **G=O holds exactly** for all QEC states

## Conclusion

G=O holds for quantum error correction codes. The equality applies to
logical entanglement in the same way as physical entanglement.
