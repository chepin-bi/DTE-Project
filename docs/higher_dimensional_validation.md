# Higher-Dimensional System Validation

## Date: 2026-09-25

## Purpose

Test if G=O holds for higher-dimensional bipartite systems (d=4,5,6).

## Results

### 4×4 System

| State | G | Diff |
|-------|---|------|
| Maximally entangled | 1.500000 | 0.00e+00 |
| Random pure | 0.988839 | 1.11e-16 |

### 5×5 System

| State | G | Diff |
|-------|---|------|
| Maximally entangled | 2.000000 | 0.00e+00 |
| Random pure | 0.986654 | 1.11e-16 |

### 6×6 System

| State | G | Diff |
|-------|---|------|
| Maximally entangled | 2.500000 | 1.33e-15 |
| Random pure | 1.907874 | 2.22e-16 |

## Observations

1. **Maximally entangled states**: G = (d−1)/2
   - d=4: G=1.5, d=5: G=2.0, d=6: G=2.5
   - Matches theoretical prediction

2. **Random pure states**: G varies
   - Typically G ≈ 0.99-1.91 for d=4-6
   - Reflects random entanglement structure

3. **G=O holds exactly** in all cases

## Conclusion

G=O holds for higher-dimensional systems up to d=6. The equality is
independent of system dimension.
