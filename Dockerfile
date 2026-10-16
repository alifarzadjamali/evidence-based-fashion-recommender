FROM python:3.11-slim

WORKDIR /workspace
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev
COPY scripts ./scripts
COPY configs ./configs
COPY data/kb ./data/kb

ENTRYPOINT ["uv", "run", "python", "scripts/run_final_pipeline.py"]
CMD ["--check"]
