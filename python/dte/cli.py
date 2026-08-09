"""
DTE Command-Line Interface
===========================

Interactive CLI for DTE analysis, batch processing, and reporting.

Usage:
    dte analyze --state bell --dims 2 2
    dte benchmark --output report.json
    dte classify --file state.npy --dims 3 3
    dte viz --type fingerprint --output fig.png
"""

import argparse
import sys
import json
import logging
from pathlib import Path
from typing import Optional, List

import numpy as np

from .core import DTECoreEngine, DTETriple
from .states import StateGenerator
from .classification import EntanglementClassifier
from .io import StateExporter, StateImporter
from .viz import DTEVisualizer
from .logging_config import setup_logging


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="dte",
        description="DTE-SIUπ-AX: Derived Triangle Equivalence Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  dte analyze --state bell --dims 2 2
  dte classify --file rho.npy --dims 3 3 --json
  dte benchmark --output report.json
  dte viz --type werner --dims 2 --output phase.png
        """
    )
    
    parser.add_argument("--version", action="version", version="%(prog)s 3.0.0")
    parser.add_argument("--verbose", "-v", action="count", default=0,
                        help="Increase verbosity (-v, -vv, -vvv)")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress output")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a quantum state")
    analyze_parser.add_argument("--state", choices=["bell", "separable", "maxent", "werner"],
                                 default="bell", help="State type")
    analyze_parser.add_argument("--dims", nargs=2, type=int, default=[2, 2],
                                 metavar=("DA", "DB"), help="Dimensions")
    analyze_parser.add_argument("--param", type=float, default=0.5,
                                 help="State parameter (e.g., Werner p)")
    analyze_parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    # classify command
    classify_parser = subparsers.add_parser("classify", help="Classify a state from file")
    classify_parser.add_argument("--file", required=True, help="Path to .npy density matrix")
    classify_parser.add_argument("--dims", nargs=2, type=int, required=True,
                                  metavar=("DA", "DB"), help="Dimensions")
    classify_parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    # benchmark command
    bench_parser = subparsers.add_parser("benchmark", help="Run standard benchmark suite")
    bench_parser.add_argument("--output", help="Save results to JSON file")
    bench_parser.add_argument("--format", choices=["text", "json"], default="text",
                               help="Output format")
    
    # viz command
    viz_parser = subparsers.add_parser("viz", help="Generate visualizations")
    viz_parser.add_argument("--type", choices=["fingerprint", "werner", "evolution"],
                            default="fingerprint", help="Visualization type")
    viz_parser.add_argument("--dims", type=int, default=2, help="Dimension for Werner plot")
    viz_parser.add_argument("--output", required=True, help="Output file path")
    
    # export command
    export_parser = subparsers.add_parser("export", help="Export state to various formats")
    export_parser.add_argument("--file", required=True, help="Input .npy file")
    export_parser.add_argument("--format", choices=["json", "yaml", "npy"],
                                required=True, help="Export format")
    export_parser.add_argument("--output", required=True, help="Output file path")
    
    return parser


def cmd_analyze(args: argparse.Namespace) -> int:
    """Execute analyze command."""
    gen = StateGenerator()
    da, db = args.dims
    
    state_map = {
        "bell": gen.bell_state,
        "separable": lambda: gen.separable_state(da, db),
        "maxent": lambda: gen.maximally_entangled(min(da, db)),
        "werner": lambda: gen.werner_state(args.param, min(da, db)),
    }
    
    try:
        rho = state_map[args.state]()
    except Exception as e:
        print(f"Error generating state: {e}", file=sys.stderr)
        return 1
    
    engine = DTECoreEngine(da, db)
    triple = engine.triple(rho)
    
    if args.json:
        print(json.dumps(triple.to_dict(), indent=2))
    else:
        print(triple)
        print(f"Classification: {triple.classify(dims=(da, db))}")
        print(f"DTE Score: {triple.DTE_score:.6f}")
        print(f"I/G^2: {triple.I_over_G2:.4f}" if triple.G > 1e-10 else "I/G^2: inf")
    
    return 0


def cmd_classify(args: argparse.Namespace) -> int:
    """Execute classify command."""
    try:
        rho = StateImporter.from_numpy(args.file)
    except Exception as e:
        print(f"Error loading state: {e}", file=sys.stderr)
        return 1
    
    da, db = args.dims
    classifier = EntanglementClassifier(da, db)
    result = classifier.classify(rho)
    
    if args.json:
        data = {
            "type": result.entanglement_type.value,
            "confidence": result.confidence,
            "triple": result.triple.to_dict(),
            "warnings": result.warnings,
        }
        print(json.dumps(data, indent=2))
    else:
        print(classifier.classify_report(rho))
    
    return 0


def cmd_benchmark(args: argparse.Namespace) -> int:
    """Execute benchmark command."""
    from .benchmark import run_benchmark_suite
    
    results = run_benchmark_suite()
    
    if args.format == "json":
        output = json.dumps(results, indent=2)
        if args.output:
            Path(args.output).write_text(output)
        else:
            print(output)
    else:
        from .benchmark import print_benchmark_report
        print_benchmark_report(results)
        if args.output:
            Path(args.output).write_text(json.dumps(results, indent=2))
    
    return 0


def cmd_viz(args: argparse.Namespace) -> int:
    """Execute viz command."""
    viz = DTEVisualizer()
    
    if args.type == "werner":
        fig = viz.werner_phase_diagram(d=args.dims, save_path=args.output)
    elif args.type == "fingerprint":
        # Generate sample states for fingerprint
        gen = StateGenerator()
        triples = []
        for p in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
            engine = DTECoreEngine(2, 2)
            triples.append(engine.triple(gen.werner_state(p, 2)))
        fig = viz.fingerprint_3d(triples, title="Werner State Fingerprint",
                                   save_path=args.output)
    else:
        print(f"Visualization type '{args.type}' not yet implemented", file=sys.stderr)
        return 1
    
    if fig is None:
        print("Visualization failed. Is matplotlib installed?", file=sys.stderr)
        return 1
    
    print(f"Saved visualization to {args.output}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    """Execute export command."""
    try:
        rho = StateImporter.from_numpy(args.file)
    except Exception as e:
        print(f"Error loading state: {e}", file=sys.stderr)
        return 1
    
    if args.format == "json":
        StateExporter.to_json(rho, args.output)
    elif args.format == "yaml":
        StateExporter.to_yaml(rho, args.output)
    elif args.format == "npy":
        StateExporter.to_numpy(rho, args.output)
    
    print(f"Exported to {args.output}")
    return 0


def main(args: Optional[List[str]] = None) -> int:
    """Main CLI entry point."""
    parser = create_parser()
    parsed = parser.parse_args(args)
    
    # Setup logging
    log_level = ["WARNING", "INFO", "DEBUG"][min(parsed.verbose, 2)]
    if parsed.quiet:
        log_level = "ERROR"
    setup_logging(level=log_level)
    
    if not parsed.command:
        parser.print_help()
        return 1
    
    commands = {
        "analyze": cmd_analyze,
        "classify": cmd_classify,
        "benchmark": cmd_benchmark,
        "viz": cmd_viz,
        "export": cmd_export,
    }
    
    return commands[parsed.command](parsed)


if __name__ == "__main__":
    sys.exit(main())
