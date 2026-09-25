# G vs Entropy Correlation

## Date: 2026-09-25

## Purpose

Study the correlation between G and von Neumann entropy for mixed states.

## Setup

Werner-like states: ρ = p|Φ⁺⟩⟨Φ⁺| + (1-p)I/4

## Results

| p | G | Entropy S | Diff |
|---|------|-----------|------|
| 0.00 | 0.0000 | 2.0000 | 0.00e+00 |
| 0.25 | 0.0000 | 1.8802 | 0.00e+00 |
| 0.50 | 0.1250 | 1.5488 | 6.94e-17 |
| 0.75 | 0.3125 | 0.9934 | 1.11e-16 |
| 1.00 | 0.5000 | 0.0000 | 1.11e-16 |

## Key Finding

**Pearson correlation G vs S: -0.9880**

Strong negative correlation between entanglement (G) and mixedness
(entropy). Pure maximally entangled states have G=0.5, S=0, while
maximally mixed states have G=0, S=2.

## Conclusion

G=O holds exactly across the full range of mixedness, and G shows strong
anti-correlation with entropy for Werner-like states.
