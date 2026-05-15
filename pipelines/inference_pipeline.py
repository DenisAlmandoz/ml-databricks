import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import argparse
from mlops_project.serving.batch_inference import run_batch_inference


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model-path", default="models/customer_value_model.json")
    args = parser.parse_args()
    print(run_batch_inference(args.input, args.output, args.model_path))
