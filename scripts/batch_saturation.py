#!/usr/bin/env python3
"""
DTE Batch Saturation Attack Runner
===================================
High-performance batch runner for million-scale DTE validation.
Designed to run on external compute (Kaggle, Colab, HPC).

Usage:
    python batch_saturation.py --samples 1000000 --dims 2 10 --output results.json
    python batch_saturation.py --theorem 1 --samples 500000 --parallel 8
"""

import argparse
import json
import time
import multiprocessing as mp
from pathlib import Path
import numpy as np

# Add parent to path for dte imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "python"))

from dte.core import DTECoreEngine
from dte.states import StateGenerator


def batch_theorem1(args):
    """Worker: validate Theorem 1 (G=O) for a batch."""
    da, db, n, seed_start = args
    eng = DTECoreEngine(da, db, validate=False)
    max_diff = 0.0
    passes = 0
    for i in range(n):
        r = (seed_start + i) % 4
        if r == 0:
            rho = StateGenerator.maximally_entangled(min(da, db))
        elif r == 1:
            rho = StateGenerator.random_mixed_state(da * db, seed=seed_start + i)
        elif r == 2:
            rho = StateGenerator.werner_state(0.3 + 0.4 * ((seed_start + i) % 10) / 10, min(da, db))
        else:
            p = 0.4 + 0.2 * ((seed_start + i) % 5) / 5
            rho = p * StateGenerator.maximally_entangled(min(da, db)) + (1 - p) * np.eye(da * db) / (da * db)
            rho = rho / np.trace(rho)
        diff = abs(eng.G(rho) - eng.O(rho))
        max_diff = max(max_diff, diff)
        if diff < 1e-7:
            passes += 1
    return {"da": da, "db": db, "passes": passes, "total": n, "max_diff": max_diff}


def batch_theorem2(args):
    """Worker: validate Theorem 2 (I >= cG^2) for a batch."""
    da, db, n, seed_start = args
    d = min(da, db)
    eng = DTECoreEngine(da, db, validate=False)
    c_d = 8.0 * np.log2(d) / ((d - 1) ** 2) if d > 1 else 8.0
    passes = 0
    min_ratio = float("inf")
    for i in range(n):
        r = (seed_start + i) % 4
        if r == 0:
            rho = StateGenerator.random_pure_state(da * db, seed=seed_start + i)
        elif r == 1:
            rho = StateGenerator.random_mixed_state(da * db, seed=seed_start + i)
        elif r == 2:
            rho = StateGenerator.werner_state(0.3 + 0.4 * ((seed_start + i) % 10) / 10, d)
        else:
            rho = StateGenerator.maximally_entangled(d)
        t = eng.triple(rho)
        if t.G > 1e-10:
            ratio = t.I / (t.G ** 2)
            min_ratio = min(min_ratio, ratio)
            if ratio >= c_d - 1e-6:
                passes += 1
        else:
            passes += 1
    return {"da": da, "db": db, "passes": passes, "total": n, "min_ratio": min_ratio}


def main():
    parser = argparse.ArgumentParser(description="DTE Batch Saturation Attack")
    parser.add_argument("--theorem", type=int, choices=[1, 2, 3, 4], default=1)
    parser.add_argument("--samples", type=int, default=100000)
    parser.add_argument("--dims", nargs=2, type=int, default=[2, 10],
                        help="Dimension range: min max")
    parser.add_argument("--parallel", type=int, default=mp.cpu_count())
    parser.add_argument("--output", type=str, default="saturation_results.json")
    parser.add_argument("--batch-size", type=int, default=1000)
    args = parser.parse_args()

    print(f"DTE Batch Saturation v3.2.0")
    print(f"Theorem: {args.theorem} | Samples: {args.samples} | Parallel: {args.parallel}")
    print("=" * 50)

    # Build work units
    min_d, max_d = args.dims
    dims = [(d, d) for d in range(min_d, max_d + 1)]
    samples_per_dim = args.samples // len(dims)

    work_units = []
    for da, db in dims:
        n_batches = samples_per_dim // args.batch_size
        for b in range(n_batches):
            work_units.append((da, db, args.batch_size, b * args.batch_size + da * 100000))
        # Remainder
        rem = samples_per_dim % args.batch_size
        if rem > 0:
            work_units.append((da, db, rem, n_batches * args.batch_size + da * 100000))

    # Execute
    worker_fn = batch_theorem1 if args.theorem == 1 else batch_theorem2
    start = time.time()

    with mp.Pool(args.parallel) as pool:
        results = pool.map(worker_fn, work_units)

    elapsed = time.time() - start

    # Aggregate
    agg = {}
    for r in results:
        key = f"{r['da']}x{r['db']}"
        if key not in agg:
            agg[key] = {"passes": 0, "total": 0, "metric": 0.0 if args.theorem == 1 else float("inf")}
        agg[key]["passes"] += r["passes"]
        agg[key]["total"] += r["total"]
        if args.theorem == 1:
            agg[key]["metric"] = max(agg[key]["metric"], r.get("max_diff", 0.0))
        else:
            agg[key]["metric"] = min(agg[key]["metric"], r.get("min_ratio", float("inf")))

    total_pass = sum(v["passes"] for v in agg.values())
    total_n = sum(v["total"] for v in agg.values())

    print(f"\nTotal: {total_pass}/{total_n} ({total_pass / total_n * 100:.2f}%)")
    print(f"Time: {elapsed:.1f}s ({total_n / elapsed:.0f} s/s)")
    for key, v in agg.items():
        print(f"  {key}: {v['passes']}/{v['total']} metric={v['metric']:.4e}")

    # Save
    output = {
        "theorem": args.theorem,
        "total_samples": total_n,
        "total_pass": total_pass,
        "rate": total_pass / total_n,
        "time": elapsed,
        "by_dimension": agg
    }
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
