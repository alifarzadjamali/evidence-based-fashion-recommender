# Evidence-constrained fashion recommendation

This pipeline recommends fashion items from image and product-text embeddings, reranks them with source-linked fashion rules, and generates explanations from the retained rule evidence. It then extracts atomic claims, verifies their support and computes paired explanation and recommendation metrics.

The target categories are tops, bottoms, shoes, outerwear and bags. The canonical input, `data/kb/fashion_rules.csv`, contains 200 rules with source references and applicability fields. These are experimental styling rules with finite coverage. CLIP fusion uses 0.40 image and 0.60 text weights; reranking uses 0.75 CLIP and 0.25 rule evidence, retaining up to five applicable rules. The settings and validation grids are in `configs/experiment.yaml`.

## Repository contents

| Path | Purpose |
|---|---|
| `src/evidence_fashion/` | Data preparation, retrieval, reranking, explanation contracts and evaluation |
| `scripts/` | Stage runners, model caching and knowledge-base checks |
| `configs/experiment.yaml` | Dataset revision, splits, candidate pools, ranking settings and output paths |
| `configs/models.yaml` | Model revisions, recorded digests and inference settings |
| `configs/prompts.yaml` | Generation, extraction and verification prompts |
| `data/kb/fashion_rules.csv` | Canonical rule input and source provenance |
| `tests/` | Functional tests for preprocessing, evidence handling and statistical analysis |
| `uv.lock` | Locked Python dependencies |

Generated data, model caches, run outputs and documents stay outside version control. A new run creates its own manifests, tables, figures and release package.

## Setup

Use Python 3.11 and uv. Run commands from the repository root.

```bash
uv sync --frozen --extra dev
uv run python scripts/cache_huggingface_models.py
```

The cache command downloads the pinned MiniLM and CLIP revisions in `configs/models.yaml`. Later stages load those models from the local cache. Data preparation downloads `Marqo/polyvore` at revision `8c782ee447faf2d2a0402ac883cf07d3b3f43e1c`, as configured in `configs/experiment.yaml`.

Start Ollama at the configured endpoint, `http://127.0.0.1:11434`, and install these model tags:

```bash
ollama pull qwen3-embedding:0.6b
ollama pull gemma4:12b
ollama pull llama3.1:8b-instruct-q8_0
ollama pull ministral-3:14b-instruct-2512-q4_K_M
ollama pull qwen3.5:9b
ollama pull phi4:14b
```

Check local model metadata against the revisions and recorded digests in `configs/models.yaml`; tags can change. Dataset preparation, embeddings and local inference require substantial disk and memory. GPU execution is recommended. For the configured CUDA dependency, add `--extra cuda` to the sync command.

## Run the pipeline

Check that Ollama and the cached embedding models are available:

```bash
uv run python scripts/run_final_pipeline.py --check
```

This loads the embedding models and queries Ollama model availability. It does not generate explanations or download the dataset.

Start a complete run:

```bash
uv run python scripts/run_final_pipeline.py --run
```

The runner executes these steps in order:

1. Prepare the dataset, enforce split and exact-image leakage controls, and construct cases.
2. Build text, image and rule embeddings; evaluate validation sensitivity and run extraction/verification integrity checks.
3. Freeze the preflight manifest, rank candidates, rerank with rule evidence and lock the selected items and traces.
4. Generate paired No-RAG and Rule-RAG explanations for the same selected items.
5. Extract atomic claims and verify them against the retained trace, full rule packet and eligible item facts.
6. Compute recommendation metrics and paired explanation contrasts, then write the release package and hashes.

Outputs default to `.runtime/reproductions/<timestamp>/`. Set `--run-root /path/to/new-run` to choose another location. The directory must not already exist. Each run contains its resolved experiment configuration, runtime records and an `artifacts/` directory with manifests, tables, figures and release files. Model responses can vary with hardware and server versions; compare recorded revisions, digests and inference settings when reproducing results.

Use `--config`, `--models-config` and `--prompts-config` to supply alternative configuration files. Individual stage scripts also expose command-line arguments through `--help`. They consume the manifests and outputs of preceding stages.

## Check the implementation

```bash
uv run --extra dev python -m pytest -q
uv run --extra dev python -m ruff check src scripts tests
```

These checks run without downloading the dataset or calling generation models. CI runs the same tests and lint checks. To regenerate rule coverage, source counts and duplicate-similarity tables locally:

```bash
uv run python scripts/rebuild_kb_audits.py --output-dir .runtime/kb-checks
```

The pipeline preserves rule IDs, evidence traces, configuration hashes and model metadata. Images contribute to recommendation embeddings; explanation evidence is drawn from the allowed product text and rule packets. Verification labels are automated source-support judgements and need separate validation for human-facing claims.

## Container execution

```bash
docker build -t evidence-fashion .
docker run --rm evidence-fashion --help
```

The image defaults to the prerequisite check. For inference, mount the Hugging Face cache and a writable run directory, and configure an Ollama endpoint reachable from the container. The default loopback endpoint refers to the container itself. Direct host execution uses the setup above.
