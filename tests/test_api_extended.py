"""Tests for DTE Extended API."""

import pytest
from fastapi.testclient import TestClient

from dte.api_extended import app

client = TestClient(app)


class TestRoot:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        assert data["version"] == "3.2.0-ext"


class TestBatchValidate:
    def test_batch_theorem1_small(self):
        response = client.post("/batch/validate", json={
            "dim_a": 2, "dim_b": 2, "n_samples": 50, "state_type": "random_mixed", "seed": 42
        })
        assert response.status_code == 200
        data = response.json()
        assert data["theorem1_rate"] > 0.95
        assert data["theorem2_rate"] > 0.90
        assert 0 <= data["mean_G"] <= 10
        assert data["mean_I"] >= 0

    def test_batch_pure_states(self):
        response = client.post("/batch/validate", json={
            "dim_a": 3, "dim_b": 3, "n_samples": 30, "state_type": "random_pure", "seed": 1
        })
        assert response.status_code == 200
        data = response.json()
        assert data["theorem1_total"] == 30

    def test_batch_too_large(self):
        response = client.post("/batch/validate", json={
            "dim_a": 2, "dim_b": 2, "n_samples": 50000
        })
        assert response.status_code == 400


class TestStatesList:
    def test_list_states(self):
        response = client.get("/states/list")
        assert response.status_code == 200
        data = response.json()
        assert len(data["states"]) >= 7
        names = [s["name"] for s in data["states"]]
        assert "bell" in names
        assert "ghz" in names
        assert "w" in names


class TestTheoremsSummary:
    def test_theorems(self):
        response = client.get("/theorems/summary")
        assert response.status_code == 200
        data = response.json()
        assert len(data["theorems"]) == 4
        ids = [t["id"] for t in data["theorems"]]
        assert ids == [1, 2, 3, 4]


class TestConjectures:
    def test_conjectures(self):
        response = client.get("/conjectures")
        assert response.status_code == 200
        data = response.json()
        assert len(data["conjectures"]) == 5
        statuses = [c["status"] for c in data["conjectures"]]
        assert "CONFIRMED" in statuses
