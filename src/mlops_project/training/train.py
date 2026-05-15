import argparse
from mlops_project.features.feature_engineering import build_features, split_xy
from mlops_project.ingestion.load_data import load_customer_data
from mlops_project.ingestion.validation import validate_customer_frame
from mlops_project.training.evaluate import evaluate_model
from mlops_project.utils.helpers import read_yaml, write_json
from mlops_project.utils.paths import resolve_path


def train_from_config(config_path: str = "configs/train_config.yaml") -> dict[str, float]:
    config = read_yaml(resolve_path(config_path))
    rows = load_customer_data(str(config["input_path"]))
    validate_customer_frame(rows)
    feature_rows = build_features(rows)
    x, y = split_xy(feature_rows, str(config["target_column"]))
    model = {
        "type": "threshold_baseline",
        "spend_threshold": sum(row["monthly_spend"] for row in x) / len(x),
        "income_threshold": sum(row["annual_income"] for row in x) / len(x),
    }
    metrics = evaluate_model(model, x, y)
    write_json(resolve_path(str(config["model_output_path"])), model)
    write_json(resolve_path(str(config["metrics_output_path"])), metrics)
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/train_config.yaml")
    args = parser.parse_args()
    print(train_from_config(args.config))


if __name__ == "__main__":
    main()
