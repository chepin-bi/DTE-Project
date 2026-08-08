FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Lean 4
RUN curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y
ENV PATH="/root/.elan/bin:${PATH}"

# Set working directory
WORKDIR /workspace

# Copy Python package
COPY python/ ./python/
COPY tests/ ./tests/
COPY setup.py .
COPY README.md .
COPY LICENSE .

# Install Python dependencies
RUN pip install --no-cache-dir -e ".[dev]"

# Copy Lean project
COPY lean/ ./lean/

# Build Lean project
RUN cd lean && lake build || true

# Run tests
RUN PYTHONPATH=python python tests/test_dte_core.py

# Default command
CMD ["python", "-c", "from dte_core import DTEBenchmark; DTEBenchmark.run_standard_tests(); DTEBenchmark.print_report(DTEBenchmark.run_standard_tests())"]
