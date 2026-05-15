import argparse
import csv
from mlops_project.ingestion.load_data import load_customer_data
from mlops_project.serving.predict import predict_records
from mlops_project.utils.paths import resolve_path


def run_batch_inference(input_path: str, output_path: str, model_path: str = "models/customer_value_model.json") -> list[dict]:
    rows = load_customer_data(input_path)
    predictions = predict_records(model_path, rows)
    result = [prediction.model_dump() for prediction in predictions]
    target = resolve_path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["customer_id", "high_value_probability", "predicted_high_value"])
        writer.writeheader()
        writer.writerows(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model-path", default="models/customer_value_model.json")
    args = parser.parse_args()
    print(run_batch_inference(args.input, args.output, args.model_path))


if __name__ == "__main__":
    main()
