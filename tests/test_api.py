"""Tests for DTE FastAPI REST service."""

import pytest
import numpy as np
from fastapi.testclient import TestClient

from dte.api import app

client = TestClient(app)


class TestRoot:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["version"] == "3.2.0"

    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"


class TestAnalyzeState:
    def test_bell_state(self):
        response = client.post("/analyze/state", json={
            "dim_a": 2, "dim_b": 2, "state_type": "bell"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["G"] == pytest.approx(0.5, abs=1e-6)
        assert data["O"] == pytest.approx(0.5, abs=1e-6)
        assert data["I"] == pytest.approx(2.0, abs=1e-6)

    def test_werner_state(self):
        response = client.post("/analyze/state", json={
            "dim_a": 3, "dim_b": 3, "state_type": "werner", "param": 0.5
        })
        assert response.status_code == 200
        data = response.json()
        assert data["dimension"] == [3, 3]
        assert data["G"] >= 0

    def test_random_mixed(self):
        response = client.post("/analyze/state", json={
            "dim_a": 4, "dim_b": 4, "state_type": "random_mixed", "seed": 42
        })
        assert response.status_code == 200
        data = response.json()
        assert 0 <= data["G"] <= 10
        assert data["I"] >= 0


class TestAnalyzeMatrix:
    def test_identity_matrix(self):
        response = client.post("/analyze/matrix", json={
            "dim_a": 2, "dim_b": 2,
            "matrix_real": [[0.25, 0, 0, 0],
                           [0, 0.25, 0, 0],
                           [0, 0, 0.25, 0],
                           [0, 0, 0, 0.25]]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["G"] == pytest.approx(0.0, abs=1e-6)

    def test_bell_matrix(self):
        response = client.post("/analyze/matrix", json={
            "dim_a": 2, "dim_b": 2,
            "matrix_real": [[0.5, 0, 0, 0.5],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0.5, 0, 0, 0.5]]
        })
        assert response.status_code == 200
        data = response.json()
        assert data["G"] == pytest.approx(0.5, abs=1e-6)


class TestClassify:
    def test_classify_bell(self):
        response = client.post("/classify", json={
            "dim_a": 2, "dim_b": 2, "state_type": "bell"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["npt"] is True
        assert data["separable"] is False
        assert data["g_value"] == pytest.approx(0.5, abs=1e-6)


class TestBenchmark:
    def test_benchmark(self):
        response = client.get("/benchmark")
        assert response.status_code == 200
        data = response.json()
        assert "benchmarks" in data
        assert len(data["benchmarks"]) == 3
