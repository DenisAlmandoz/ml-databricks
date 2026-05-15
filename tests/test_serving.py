from mlops_project.ingestion.load_data import load_customer_data
from mlops_project.serving.predict import predict_records
from mlops_project.training.train import train_from_config


def test_predict_records(tmp_path):
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
    train_from_config(str(config))
    records = load_customer_data("data/raw/customers.csv")[:2]
    predictions = predict_records(str(model_path), records)
    assert len(predictions) == 2
    assert all(0 <= item.high_value_probability <= 1 for item in predictions)
