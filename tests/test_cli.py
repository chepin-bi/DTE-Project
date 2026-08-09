"""
DTE CLI Tests
=============
"""

import sys
sys.path.insert(0, '/mnt/agents/output/DTE-Project/python')

from dte.cli import create_parser, main


def test_parser_help():
    parser = create_parser()
    # Should not raise
    assert parser is not None


def test_analyze_command():
    rc = main(["analyze", "--state", "bell", "--dims", "2", "2", "--json"])
    assert rc == 0


def test_benchmark_command():
    rc = main(["benchmark", "--format", "json"])
    assert rc == 0


def test_viz_command_without_matplotlib():
    # Should fail gracefully if matplotlib not installed
    rc = main(["viz", "--type", "werner", "--dims", "2", "--output", "/tmp/test_viz.png"])
    # May fail if matplotlib missing, but should not crash
    assert rc in (0, 1)
