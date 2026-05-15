from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="customer_value_training",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "fundamentals"],
) as dag:
    train = BashOperator(
        task_id="train_model",
        bash_command="uv run python pipelines/training_pipeline.py --config configs/train_config.yaml",
    )

    batch_inference = BashOperator(
        task_id="batch_inference",
        bash_command="uv run python pipelines/inference_pipeline.py --input data/raw/customers.csv --output data/processed/predictions.csv",
    )

    train >> batch_inference
