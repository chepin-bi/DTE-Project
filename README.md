# DTE-SIUπ-AX: Derived Triangle Equivalence Unified Framework

[![Tests](https://img.shields.io/badge/tests-28%2F28%20passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.8+-blue)]()
[![Lean](https://img.shields.io/badge/lean-4.x-purple)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![PyPI](https://img.shields.io/badge/pypi-dte--core-blue)]()

> **A computable, strict, and complete implementation of the DTE-SIUπ-AX framework for quantum entanglement analysis, holography, neuroscience, and beyond.**

## Overview

The Derived Triangle Equivalence (DTE) framework unifies quantum entanglement analysis through a **triple invariant** (G, I, O):

| Face | Symbol | Formula | Physical Meaning |
|------|--------|---------|-----------------|
| **Geometric** | G | (||ρ^T_A||₁ - 1)/2 | Negativity = Ext¹ |
| **Information** | I | S(ρ_A) + S(ρ_B) - S(ρ) | Mutual Information |
| **Open** | O | Σ_{λ_i<0}\|λ_i\| | Boundary Obstruction |

**Theorem 1**: G = O exactly (all dimensions)
**Theorem 2**: I ≥ c(d)·G² where c(d) = 8log₂d/(d-1)²
**Theorem 3**: G=I=O=0 ⟺ separable (2×2, 2×3)
**Theorem 4**: PPT-bound entangled exists (d≥3)

## Installation

```bash
pip install dte-core
```

With extras:
```bash
pip install dte-core[viz]      # matplotlib visualizations
pip install dte-core[api]      # FastAPI web service
pip install dte-core[dev]      # pytest, black, mypy
pip install dte-core[all]      # everything
```

## Quick Start

### Python API

```python
from dte import DTECoreEngine, StateGenerator, EntanglementClassifier

# Initialize engine
engine = DTECoreEngine(dim_a=2, dim_b=2)

# Analyze a Bell state
rho = StateGenerator.bell_state()
triple = engine.triple(rho)
print(triple)
# DTETriple(G=0.500000, I=2.000000, O=0.500000)

# Classify with confidence
classifier = EntanglementClassifier(2, 2)
result = classifier.classify(rho)
print(result.entanglement_type)  # NPT ENTANGLED
print(f"Confidence: {result.confidence:.1%}")
```

### CLI

```bash
# Analyze standard states
dte analyze --state bell --dims 2 2 --json
dte analyze --state werner --param 0.5 --dims 3 3

# Run benchmarks
dte benchmark --format json --output report.json

# Generate visualizations
dte viz --type werner --dims 2 --output phase.png
dte viz --type fingerprint --output fingerprint.png

# Classify from file
dte classify --file state.npy --dims 3 3 --json
```

### Web API

```bash
pip install dte-core[api]
uvicorn dte.api:app --host 0.0.0.0 --port 8080
```

Then visit `http://localhost:8080/docs` for interactive API documentation.

## Architecture

```
dte/
├── core.py           # DTECoreEngine, DTETriple, EntanglementType
├── states.py         # StateGenerator (Bell, Werner, GHZ, W, etc.)
├── classification.py # EntanglementClassifier with confidence scoring
├── io.py             # Import/export (Qiskit, QuTiP, JSON, YAML, NumPy)
├── viz.py            # 3D fingerprint, evolution plots, phase diagrams
├── cli.py            # Command-line interface
├── api.py            # FastAPI REST service
├── config.py         # DTEConfig (YAML, JSON, env vars)
├── benchmark.py      # Performance and correctness benchmarks
├── utils.py          # Validation, Schmidt decomposition, fidelity
├── exceptions.py     # Structured exception hierarchy
└── logging_config.py # Structured logging setup
```

## Project Structure

```
DTE-Project/
├── python/dte/           # Main Python package
├── tests/                # pytest test suite
├── lean/DTE/             # Lean 4 formalization
├── docs/                 # Theory docs, paradigm analysis, roadmaps
├── formal/               # LaTeX paper
├── examples/             # Usage examples
├── .github/workflows/    # CI/CD (Python + Lean 4)
├── Dockerfile            # Container image
└── docker-compose.yml    # Full stack deployment
```

## Cross-Paradigm Isomorphisms

DTE's triadic structure appears across mathematics and physics:

| Paradigm | G (Geometry) | I (Information) | O (Open) |
|----------|-------------|-----------------|----------|
| Atiyah-Singer | ch(E) | Index(D) | [E] ∈ K(X) |
| Mirror Symmetry | Dᵇ(Coh X) | Fukaya(Xᵛ) | SYZ |
| Langlands | Bun_G(X) | LocSys | Hecke |
| Factorization Homology | Eₙ-algebra | ∫_M A | TQFT |
| Cat. Quantum Mechanics | Hilbert space | String diagrams | Channel |
| Comp. Game Theory | Strategy space | Nash equilibrium | Open games |
| **DTE (This Work)** | **Ext¹ = N(ρ)** | **I(A:B)** | **Σ\|λ₋\|** |
| Holography | Area(γ_A)/4G_N | S_CFT(ρ) | Entanglement wedge |
| IIT (Consciousness) | Cause-effect | Φ (phi) | Exclusion |
| Economics | Market concentration | Info coupling | Barriers |

## Development

```bash
git clone https://github.com/chepin-ai/DTE-Project.git
cd DTE-Project
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run benchmarks
python -m dte.cli benchmark

# Code quality
black python/
flake8 python/
mypy python/dte/

# Build Lean
cd lean && lake build
```

## Docker

```bash
docker-compose up dte-core      # Run tests
docker-compose up dte-jupyter  # Launch Jupyter notebook
```

## Roadmap

| Phase | Status | Description |
|-------|--------|-------------|
| P0 | ✅ Complete | Core theorems, numerical verification |
| P1 | ✅ Complete | Open problems #1-#4, Lean framework |
| P2 | ✅ Complete | Cross-domain docs, holography, neuroscience, economics |
| P3 | 🔄 Current | **Lean proof completion, arXiv submission, PyPI release** |
| P4 | 📋 Planned | Infinite dimensions, quantum algorithms, experimental validation |

## Citation

```bibtex
@article{DTE2026,
  title={DTE-Generalized: A Unified Triple Framework for Quantum Entanglement},
  author={SAG-ISU-UHODP-DTE Research Group},
  year={2026},
  url={https://github.com/chepin-ai/DTE-Project}
}
```

## License

MIT License — see [LICENSE](LICENSE).

**Contact**: chepin@163.com  
**Version**: 3.0.0  
**Last Updated**: 2026-08-09
