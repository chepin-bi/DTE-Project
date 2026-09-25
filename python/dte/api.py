"""FastAPI REST service for DTE Framework."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Tuple
import numpy as np

from .core import DTECoreEngine, DTETriple
from .states import StateGenerator
from .classification import EntanglementClassifier

app = FastAPI(
    title="DTE Framework API",
    description="Derived Triangle Equivalence for quantum entanglement analysis",
    version="3.2.0",
)


class StateRequest(BaseModel):
    dim_a: int = 2
    dim_b: int = 2
    state_type: str = "random_mixed"  # bell, werner, ghz, w, random_mixed, random_pure
    param: Optional[float] = None
    seed: Optional[int] = None


class MatrixRequest(BaseModel):
    dim_a: int = 2
    dim_b: int = 2
    matrix_real: List[List[float]]
    matrix_imag: Optional[List[List[float]]] = None


class TripleResponse(BaseModel):
    G: float
    I: float
    O: float
    dimension: Tuple[int, int]


class ClassificationResponse(BaseModel):
    entanglement_type: str
    confidence: float
    npt: bool
    separable: bool
    g_value: float


@app.get("/")
def root():
    return {"message": "DTE Framework v3.2.0", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok", "version": "3.2.0"}


@app.post("/analyze/state", response_model=TripleResponse)
def analyze_state(req: StateRequest):
    try:
        eng = DTECoreEngine(req.dim_a, req.dim_b)
        
        if req.state_type == "bell":
            rho = StateGenerator.bell_state()
        elif req.state_type == "werner":
            p = req.param if req.param is not None else 0.5
            rho = StateGenerator.werner_state(p, min(req.dim_a, req.dim_b))
        elif req.state_type == "ghz":
            d = min(req.dim_a, req.dim_b)
            rho = StateGenerator.ghz_state(d)
        elif req.state_type == "w":
            d = min(req.dim_a, req.dim_b)
            rho = StateGenerator.w_state(d)
        elif req.state_type == "random_pure":
            rho = StateGenerator.random_pure_state(req.dim_a * req.dim_b, seed=req.seed)
        else:
            rho = StateGenerator.random_mixed_state(req.dim_a * req.dim_b, seed=req.seed)
        
        triple = eng.triple(rho)
        return TripleResponse(
            G=float(triple.G),
            I=float(triple.I),
            O=float(triple.O),
            dimension=(req.dim_a, req.dim_b)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/analyze/matrix", response_model=TripleResponse)
def analyze_matrix(req: MatrixRequest):
    try:
        d = req.dim_a * req.dim_b
        if len(req.matrix_real) != d or any(len(row) != d for row in req.matrix_real):
            raise ValueError(f"Matrix must be {d}x{d}")
        
        real = np.array(req.matrix_real)
        if req.matrix_imag:
            imag = np.array(req.matrix_imag)
            rho = real + 1j * imag
        else:
            rho = real.astype(complex)
        
        # Normalize trace
        rho = rho / np.trace(rho)
        
        eng = DTECoreEngine(req.dim_a, req.dim_b)
        triple = eng.triple(rho)
        return TripleResponse(
            G=float(triple.G),
            I=float(triple.I),
            O=float(triple.O),
            dimension=(req.dim_a, req.dim_b)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/classify", response_model=ClassificationResponse)
def classify_state(req: StateRequest):
    try:
        eng = DTECoreEngine(req.dim_a, req.dim_b)
        classifier = EntanglementClassifier(req.dim_a, req.dim_b)
        
        if req.state_type == "bell":
            rho = StateGenerator.bell_state()
        elif req.state_type == "werner":
            p = req.param if req.param is not None else 0.5
            rho = StateGenerator.werner_state(p, min(req.dim_a, req.dim_b))
        else:
            rho = StateGenerator.random_mixed_state(req.dim_a * req.dim_b, seed=req.seed)
        
        triple = eng.triple(rho)
        result = classifier.classify(rho)
        
        return ClassificationResponse(
            entanglement_type=result.entanglement_type.name,
            confidence=float(result.confidence),
            npt=result.npt,
            separable=result.separable,
            g_value=float(triple.G)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/benchmark")
def benchmark():
    """Run a quick benchmark."""
    import time
    dims = [(2, 2), (3, 3), (4, 4)]
    results = []
    for da, db in dims:
        start = time.time()
        eng = DTECoreEngine(da, db)
        for _ in range(100):
            rho = StateGenerator.random_mixed_state(da * db)
            eng.triple(rho)
        elapsed = time.time() - start
        results.append({"dims": f"{da}x{db}", "time_ms": round(elapsed * 10, 2)})
    return {"benchmarks": results}
