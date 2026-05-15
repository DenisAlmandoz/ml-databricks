from pathlib import Path
from mlops_project.training.train import train_from_config


def test_train_from_config_creates_metrics_and_model(tmp_path):
    config = tmp_path / "train_config.yaml"
    model_path = tmp_path / "model.json"
    metrics_path = tmp_path / "metrics.json"
    config.write_text(f"""
input_path: data/raw/customers.csv
model_output_path: {model_path}
metrics_output_path: {metrics_path}
target_column: high_value
random_state: 42
test_size: 0.25
""")
    metrics = train_from_config(str(config))
    assert Path(model_path).exists()
    assert Path(metrics_path).exists()
    assert set(metrics) == {"accuracy", "f1", "roc_auc"}
