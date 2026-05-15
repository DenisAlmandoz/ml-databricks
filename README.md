# MLOps Fundamentals on Databricks

A deliberately small, end-to-end MLOps project that demonstrates the moving parts you asked for without hiding the basics behind a large framework.  The sample problem predicts whether a customer is high value from a tiny CSV dataset.

## What is included

- **Data ingestion and validation** with Pydantic schemas and a Great Expectations-style checkpoint.
- **Data contracts** under `contracts/` that document the required columns and allowed values.
- **Feature engineering and feature lineage** that records raw-to-feature dependencies.
- **Training, metrics, explainability, and registry stubs** for a scikit-learn model.
- **Distributed training and GPU support configs** to show how those concerns are wired in.
- **Batch/online serving, canary deployment, and A/B testing** examples.
- **Monitoring** examples for drift, structured logging, and alert routing.
- **Airflow orchestration**, **Databricks Asset Bundle**, **Docker**, **Kubernetes**, **Terraform**, and **GitHub Actions** starter files.
- **Secrets management** via Pydantic settings sourced from environment variables or `.env`.

## Repository layout

```text
configs/                 Runtime, training, logging, GPU, and distributed configs
contracts/               Data contract for the sample customer dataset
data/raw/customers.csv   Tiny CSV used by tests and local runs
deployment/              Databricks, Docker, Kubernetes, Terraform, canary and A/B configs
dags/                    Airflow DAG for the local training flow
great_expectations/      Minimal expectation/checkpoint examples
lineage/                 Feature lineage graph produced/maintained by feature jobs
pipelines/               Thin orchestration entrypoints
src/mlops_project/       Python package with schemas, settings, ingestion, features, training, serving, monitoring
tests/                   Unit tests for the core fundamentals
```

## Quick start with uv

```bash
uv sync
uv run pytest
uv run python pipelines/training_pipeline.py --config configs/train_config.yaml
uv run python pipelines/inference_pipeline.py --input data/raw/customers.csv --output data/processed/predictions.csv
```

## Configuration and secrets

Copy `.env.example` to `.env` for local development.  The app loads settings from environment variables using `pydantic-settings`; production deployments should inject secrets through Databricks secret scopes, Kubernetes Secrets, or a cloud secret manager rather than committing them.

## Learning path

1. Inspect `contracts/customer_contract.yaml` and `src/mlops_project/schemas.py`.
2. Run `uv run pytest` to see validation, feature, training, and serving checks.
3. Run the training pipeline and inspect `models/metrics.json` and `lineage/feature_lineage.json`.
4. Compare deployment options in `deployment/` and orchestration in `dags/customer_value_dag.py`.
