# Contributing to DTE-Core

Thank you for your interest in contributing to the DTE-SIUπ-AX framework!

## Ways to Contribute

### 1. Mathematical Contributions
- **Theorem Proofs**: Fill `sorry` placeholders in Lean 4 files
- **Open Problems**: Attack problems listed in `docs/Open_Problems.md`
- **New Paradigms**: Add cross-paradigm isomorphisms

### 2. Engineering Contributions
- **Python Engine**: Performance optimizations, new features
- **Lean Formalization**: Complete proofs, add new theorems
- **Tests**: Expand test coverage, add property-based tests
- **Documentation**: Improve clarity, add examples

### 3. Cross-Domain Applications
- **Quantum Gravity**: Apply DTE to holographic entanglement
- **Neuroscience**: fMRI/EEG data analysis
- **Economics**: Game-theoretic applications
- **AI**: Integration with neural network interpretability

## Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/DTE-Project.git
cd DTE-Project

# Python setup
pip install -e ".[dev]"

# Run tests
PYTHONPATH=python python tests/test_dte_core.py

# Lean setup
cd lean
lake build
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## Code Standards

### Python
- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings for all public functions
- Maintain test coverage above 90%

### Lean 4
- Use Mathlib conventions
- Provide proof sketches in comments
- Mark incomplete proofs with `sorry` and `TODO`

## Open Problem Priority

| Priority | Problem | Status | Difficulty |
|----------|---------|--------|------------|
| P0 | Prove c(d) = 8log₂d/(d-1)² | 🔄 DeepSeek proof for d=2 | Medium |
| P0 | G = O strict proof | ✅ Complete | Low |
| P1 | PPT-bound entangled search | ✅ Numerical | Medium |
| P1 | DTE-Bures distance | 🔄 Numerical | High |
| P2 | Generalize to infinite dim | 📋 Open | Very High |
| P2 | Quantum gravity coupling | 📋 Open | Very High |

## Communication

- Email: chepin@163.com
- Issues: Use GitHub issue templates
- Discussions: Use GitHub Discussions for questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
