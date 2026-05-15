import csv
from mlops_project.utils.paths import resolve_path


def load_customer_data(path: str = "data/raw/customers.csv") -> list[dict]:
    with resolve_path(path).open(newline="") as f:
        return list(csv.DictReader(f))
