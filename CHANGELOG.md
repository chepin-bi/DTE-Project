# Changelog

All notable changes to the DTE Framework.

## [3.2.0-dev] - 2026-08-09

### Added
- **Multi-party G=O validation**: Verified CONJECTURE-1 for 3-party (6,000/6,000) and 4-party (2,800/2,800) systems
- **High-dimensional saturation**: Extended numerical validation to 10×10 dimensions
- **FastAPI REST API**: `/analyze/state`, `/analyze/matrix`, `/classify`, `/benchmark` endpoints
- **Docker support**: Multi-stage Dockerfile + docker-compose.yml for Python/Lean/Jupyter services
- **CI/CD configuration**: GitHub Actions workflow for Python tests, Lean build, Docker build
- **Batch saturation runner**: `scripts/batch_saturation.py` for million-scale external compute
- **Kaggle notebook template**: `kaggle/dte-batch-saturation-template.ipynb`
- **PyPI release script**: `scripts/pypi_release.sh`
- **Live dashboard**: Deployed at https://wnughdfmkz4se.ok.kimi.link
- **API tests**: 9/9 passing (`tests/test_api.py`)
- **Local lemma library**: `lean/DTE/LocalLemmas.lean` for Mathlib gaps
- **Filled proof attempts**: `DensityMatrix_Filled.lean`, `Negativity_Filled.lean`, `Theorem2_Filled.lean`, `Classification_Filled.lean`, `Attestation_Filled.lean`

### Changed
- **Test suite**: 39 → 69 tests (added API tests, multi-party tests)
- **README**: Updated badges, dashboard link, multi-party results
- **Core.lean**: Integrated all Filled modules

### Fixed
- **API `EntanglementType`**: Fixed import issue in `api.py`
- **`root()` endpoint**: Added `version` field for dashboard compatibility

## [3.1.1] - 2026-08-09

### Added
- Meta-audit system: 76 raw entries → 21 independent problem groups
- Situational awareness dashboard (matplotlib PNG)
- Technical debt tracker: 22 sorry locations with priorities
- Attestation full report: 430 CFTS requests audited

### Changed
- pyproject.toml: Added dependency groups (viz, api, neuro, finance, dev, all)

## [3.1.0] - 2026-08-09

### Added
- Complete arXiv paper LaTeX source (`formal/DTE_paper_arxiv_v3.1.0.tex`)
- Lean 4 v4.15.0 formalization framework (9 modules, 749 lines)
- Python numerical validation suite (234K+ samples)
- Kaggle notebook (`dte-saturation-attack-v3.1.0.ipynb`)

## [3.0.0] - Earlier

### Added
- Core DTE theorems (1-4)
- Python package (`dte-core`)
- Initial Lean formalization
- Cross-domain applications (holography, neuroscience, economics)
