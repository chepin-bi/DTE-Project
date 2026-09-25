# DTE Framework User Guide

## Quick Start

### Installation

```bash
pip install dte-core
```

Or from source:
```bash
git clone https://github.com/chepin-ai/DTE-Project.git
cd DTE-Project
pip install -e ".[all]"
```

### Basic Usage

```python
from dte.core import DTECoreEngine
from dte.states import StateGenerator

# Create engine for 3x3 system
eng = DTECoreEngine(3, 3)

# Analyze a Bell state
rho = StateGenerator.bell_state()
triple = eng.triple(rho)

print(f"G = {triple.G}")  # Negativity
print(f"I = {triple.I}")  # Mutual Information
print(f"O = {triple.O}")  # Boundary Obstruction
```

### REST API

Start the server:
```bash
uvicorn dte.api:app --host 0.0.0.0 --port 8080
```

Query:
```bash
curl -X POST http://localhost:8080/analyze/state \
  -H "Content-Type: application/json" \
  -d '{"dim_a": 2, "dim_b": 2, "state_type": "bell"}'
```

Response:
```json
{
  "G": 0.5,
  "I": 2.0,
  "O": 0.5,
  "dimension": [2, 2]
}
```

## State Types

| Type | Description | Parameters |
|------|-------------|------------|
| `bell` | Bell state | — |
| `ghz` | GHZ state | `dim_a`, `dim_b` |
| `w` | W state | `dim_a`, `dim_b` |
| `werner` | Werner state | `param` (mixing parameter) |
| `random_pure` | Random pure state | `seed` |
| `random_mixed` | Random mixed state | `seed` |

## Classification

```python
from dte.classification import EntanglementClassifier

classifier = EntanglementClassifier(3, 3)
result = classifier.classify(rho)

print(result.entanglement_type)  # SEPARABLE, ENTANGLED, PPT_BOUND, etc.
print(result.confidence)
```

## Docker

```bash
docker-compose up dte-api
```

## Dashboard

Live situational awareness:
https://wnughdfmkz4se.ok.kimi.link

## Citation

If you use DTE in your research, please cite:

```bibtex
@article{dte2026,
  title={Derived Triangle Equivalence Framework for Quantum Entanglement},
  author={DTE Research Group},
  year={2026}
}
```
