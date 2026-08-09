"""
DTE Web API (FastAPI)
=====================

RESTful API for remote DTE analysis.

Run:
    uvicorn dte.api:app --host 0.0.0.0 --port 8080

Or via CLI:
    dte-api  # if entry point is configured
"""

from typing import List, Dict, Any, Optional
import numpy as np

from .core import DTECoreEngine, DTETriple, EntanglementType
from .states import StateGenerator
from .classification import EntanglementClassifier

# FastAPI is optional
try:
    from fastapi import FastAPI, HTTPException, Body
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel, Field
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    FastAPI = object
    BaseModel = object
    Field = lambda *a, **k: None


if HAS_FASTAPI:
    
    app = FastAPI(
        title="DTE-SIUπ-AX API",
        description="Derived Triangle Equivalence framework for quantum entanglement analysis",
        version="3.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    
    class StateRequest(BaseModel):
        """Request to analyze a quantum state."""
        dim_a: int = Field(..., ge=2, le=1024, description="Dimension of subsystem A")
        dim_b: int = Field(..., ge=2, le=1024, description="Dimension of subsystem B")
        state_type: str = Field("random", description="State type: bell, separable, werner, random")
        param: Optional[float] = Field(None, description="State parameter (e.g., Werner p)")
        density_matrix: Optional[List[List[float]]] = Field(None, description="Custom density matrix (real part)")
    
    
    class DTEResponse(BaseModel):
        """DTE analysis response."""
        G: float = Field(..., description="Geometric face = Negativity")
        I: float = Field(..., description="Information face = Mutual Information")
        O: float = Field(..., description="Open face = Boundary Obstruction")
        classification: str = Field(..., description="Entanglement classification")
        confidence: float = Field(..., description="Classification confidence")
        dte_score: float = Field(..., description="Composite DTE score")
        theorem1_verified: bool = Field(..., description="G = O verification")
        theorem2_ratio: Optional[float] = Field(None, description="I/G^2 ratio")
    
    
    @app.get("/")
    async def root() -> Dict[str, str]:
        """API status endpoint."""
        return {
            "name": "DTE-SIUπ-AX API",
            "version": "3.0.0",
            "status": "running",
            "endpoints": ["/analyze", "/classify", "/states", "/health"]
        }
    
    
    @app.get("/health")
    async def health() -> Dict[str, str]:
        """Health check."""
        return {"status": "healthy"}
    
    
    @app.post("/analyze", response_model=DTEResponse)
    async def analyze(request: StateRequest) -> Dict[str, Any]:
        """
        Analyze a quantum state and return DTE triple.
        """
        try:
            gen = StateGenerator()
            
            # Generate or use provided state
            if request.density_matrix is not None:
                rho = np.array(request.density_matrix)
                if rho.ndim == 2:
                    rho = rho + 0j  # Make complex
            else:
                if request.state_type == "bell":
                    rho = gen.bell_state()
                elif request.state_type == "separable":
                    rho = gen.separable_state(request.dim_a, request.dim_b)
                elif request.state_type == "werner":
                    p = request.param if request.param is not None else 0.5
                    rho = gen.werner_state(p, min(request.dim_a, request.dim_b))
                elif request.state_type == "maxent":
                    rho = gen.maximally_entangled(min(request.dim_a, request.dim_b))
                else:
                    rho = gen.random_mixed_state(request.dim_a * request.dim_b)
            
            # Compute DTE
            engine = DTECoreEngine(request.dim_a, request.dim_b)
            triple = engine.triple(rho)
            
            # Verify theorems
            t1_passed, t1_diff = engine.theorem1_verify(rho)
            t2_passed, t2_ratio = engine.theorem2_verify(rho)
            
            # Classify
            classifier = EntanglementClassifier(request.dim_a, request.dim_b)
            result = classifier.classify(rho)
            
            return {
                "G": triple.G,
                "I": triple.I,
                "O": triple.O,
                "classification": result.entanglement_type.value,
                "confidence": result.confidence,
                "dte_score": triple.DTE_score,
                "theorem1_verified": t1_passed,
                "theorem2_ratio": t2_ratio if np.isfinite(t2_ratio) else None,
            }
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    
    @app.get("/states")
    async def list_states() -> Dict[str, Any]:
        """List available standard states."""
        return {
            "states": [
                {"name": "bell", "description": "Bell state |Phi+>", "dims": "2x2"},
                {"name": "separable", "description": "Product state |0,0>", "dims": "any"},
                {"name": "werner", "description": "Werner state", "params": ["p"]},
                {"name": "maxent", "description": "Maximally entangled state", "dims": "dxd"},
                {"name": "random", "description": "Random mixed state", "dims": "any"},
            ]
        }
    
    
    @app.post("/batch")
    async def batch_analyze(requests: List[StateRequest]) -> List[DTEResponse]:
        """Analyze multiple states in batch."""
        results = []
        for req in requests:
            result = await analyze(req)
            results.append(result)
        return results

else:
    # Stub when FastAPI is not installed
    app = None
    
    def _raise_import_error():
        raise ImportError(
            "FastAPI and uvicorn required for API. "
            "Install with: pip install dte-core[api]"
        )
