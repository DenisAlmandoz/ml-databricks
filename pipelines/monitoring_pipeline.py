import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mlops_project.ingestion.load_data import load_customer_data
from mlops_project.monitoring.alerts import build_drift_alert
from mlops_project.monitoring.drift import mean_drift


def run_monitoring(reference_path: str, current_path: str, threshold: float, destination: str):
    drift = mean_drift(load_customer_data(reference_path), load_customer_data(current_path), "monthly_spend")
    return build_drift_alert("monthly_spend", drift, threshold, destination)
