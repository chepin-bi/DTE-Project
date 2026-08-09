"""
DTE Benchmark Suite
===================

Comprehensive benchmarks for theorem verification, performance, and correctness.
"""

import time
import numpy as np
from typing import Dict, Any, List, Tuple
import logging

from .core import DTECoreEngine, DTETriple
from .states import StateGenerator

logger = logging.getLogger("dte.benchmark")


def run_benchmark_suite() -> Dict[str, Any]:
    """Run the complete DTE benchmark suite."""
    results = {
        "metadata": {
            "numpy_version": np.__version__,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "tests": {},
        "performance": {},
    }
    
    gen = StateGenerator()
    
    # === Correctness Tests ===
    
    # Test 1: Bell state
    engine = DTECoreEngine(2, 2)
    bell = gen.bell_state()
    t = engine.triple(bell)
    results["tests"]["bell_22"] = {
        "triple": t.to_dict(),
        "theorem1": engine.theorem1_verify(bell),
        "theorem2": engine.theorem2_verify(bell),
        "expected": {"G": 0.5, "I": 2.0, "O": 0.5},
    }
    
    # Test 2: Separable state
    sep = gen.separable_state()
    t = engine.triple(sep)
    results["tests"]["separable_22"] = {
        "triple": t.to_dict(),
        "all_zero": t.G < 1e-10 and t.I < 1e-10 and t.O < 1e-10,
    }
    
    # Test 3: Werner states
    for p in [0.0, 0.3, 0.6, 1.0]:
        werner = gen.werner_state(p, 2)
        t = engine.triple(werner)
        results["tests"][f"werner_p{p}_22"] = {
            "triple": t.to_dict(),
            "theorem1": engine.theorem1_verify(werner),
        }
    
    # Test 4: 3x3 maximally entangled
    engine_33 = DTECoreEngine(3, 3)
    max_ent = gen.maximally_entangled(3)
    t = engine_33.triple(max_ent)
    results["tests"]["max_entangled_33"] = {
        "triple": t.to_dict(),
        "theorem1": engine_33.theorem1_verify(max_ent),
        "expected_G": 1.0,
    }
    
    # === Performance Tests ===
    
    # Benchmark G=O numerical precision
    max_diff = 0.0
    start = time.time()
    for seed in range(200):
        rho = gen.random_pure_state(4, seed=seed)
        diff = abs(engine.G(rho) - engine.O(rho))
        max_diff = max(max_diff, diff)
    elapsed = time.time() - start
    results["performance"]["theorem1_precision"] = {
        "max_diff": max_diff,
        "samples": 200,
        "time_sec": elapsed,
    }
    
    # Benchmark Theorem 2
    min_ratio = float('inf')
    start = time.time()
    for seed in range(200):
        rho = gen.random_pure_state(4, seed=seed)
        t = engine.triple(rho)
        if t.G > 1e-10:
            ratio = t.I / (t.G ** 2)
            min_ratio = min(min_ratio, ratio)
    elapsed = time.time() - start
    results["performance"]["theorem2_search"] = {
        "min_ratio": min_ratio,
        "theoretical_c_d": 8.0,
        "samples": 200,
        "time_sec": elapsed,
    }
    
    # Benchmark scaling
    dims = [(2, 2), (3, 3), (4, 4), (5, 5)]
    scaling_results = []
    for da, db in dims:
        eng = DTECoreEngine(da, db)
        rho = gen.random_mixed_state(da * db, seed=42)
        start = time.time()
        eng.triple(rho)
        elapsed = time.time() - start
        scaling_results.append({
            "dims": f"{da}x{db}",
            "d_total": da * db,
            "time_ms": elapsed * 1000,
        })
    results["performance"]["scaling"] = scaling_results
    
    return results


def print_benchmark_report(results: Dict[str, Any]) -> None:
    """Print formatted benchmark report."""
    print("=" * 70)
    print("DTE Benchmark Report v3.0")
    print("=" * 70)
    
    # Correctness
    print("\n[Correctness Tests]")
    print("-" * 50)
    all_pass = True
    for name, data in results["tests"].items():
        if "triple" in data:
            t = data["triple"]
            cls = t.get("classification", "N/A")
            print(f"  {name:25s} G={t['G']:7.4f} I={t['I']:7.4f} O={t['O']:7.4f} | {cls}")
        
        if "theorem1" in data:
            passed, diff = data["theorem1"]
            status = "PASS" if passed else "FAIL"
            all_pass = all_pass and passed
            print(f"    Theorem 1: {status} |G-O|={diff:.2e}")
        
        if "all_zero" in data:
            status = "PASS" if data["all_zero"] else "FAIL"
            all_pass = all_pass and data["all_zero"]
            print(f"    Separable check: {status}")
    
    # Performance
    print("\n[Performance]")
    print("-" * 50)
    perf = results["performance"]
    
    if "theorem1_precision" in perf:
        p = perf["theorem1_precision"]
        print(f"  Theorem 1 precision: max_diff={p['max_diff']:.2e} ({p['samples']} samples, {p['time_sec']:.2f}s)")
    
    if "theorem2_search" in perf:
        p = perf["theorem2_search"]
        print(f"  Theorem 2 search: min_ratio={p['min_ratio']:.4f} >= {p['theoretical_c_d']:.4f} ({p['samples']} samples, {p['time_sec']:.2f}s)")
    
    if "scaling" in perf:
        print(f"\n  Scaling:")
        for s in perf["scaling"]:
            print(f"    {s['dims']:6s} (d={s['d_total']:3d}): {s['time_ms']:7.3f} ms")
    
    print("\n" + "=" * 70)
    print(f"Overall: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    print("=" * 70)
