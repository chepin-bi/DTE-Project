# Contributing to DTE Framework

Thank you for your interest in contributing to the Derived Triangle Equivalence (DTE) Framework!

## Getting Started

### Prerequisites
- Python 3.8+
- Lean 4 (for formalization)
- Git

### Setup

```bash
git clone https://github.com/chepin-ai/DTE-Project.git
cd DTE-Project

# Python
pip install -e ".[dev]"

# Lean
cd lean
lake build
```

## Development Workflow

### Running Tests

```bash
# Python tests
pytest tests/ -v

# Specific test file
pytest tests/test_api.py -v

# With coverage
pytest tests/ --cov=dte --cov-report=html
```

### Lean Development

```bash
cd lean
lake build

# Check sorry count
grep -r 'sorry' DTE/ | wc -l
```

## Contribution Areas

### High Priority
1. **Lean sorry filling**: 22 sorry remain across 6 modules
   - P1 (6): `DensityMatrix` — partial trace properties
   - P2 (6): `Negativity`, `Theorem2` — spectral theory
   - P3-P4 (10): `Classification`, `Attestation`
2. **Mathlib PRs**: `sum_star`, `reindexing` lemmas

### Medium Priority
3. **Numerical validation**: Run batch saturation on external compute
4. **Documentation**: Improve proof strategy documentation
5. **Performance**: Optimize 10×10+ matrix operations

### Low Priority
6. **Web interface**: React/Vue frontend for API
7. **GPU acceleration**: CuPy backend
8. **Qiskit/QuTiP integration**

## Code Style

### Python
- Follow PEP 8
- Use type hints
- Docstrings for all public functions

### Lean
- Use `by` tactic blocks for complex proofs
- Comment sorry with proof strategy
- Reference Mathlib lemmas explicitly

## Commit Messages

Use Conventional Commits:
```
feat: add new theorem validation
fix: correct eigenvalue computation
docs: update proof strategy
test: add API endpoint tests
```

## Contact

- Issues: GitHub Issues
- Email: chepin@163.com
