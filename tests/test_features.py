from mlops_project.features.feature_engineering import build_features
from mlops_project.ingestion.load_data import load_customer_data
from mlops_project.ingestion.validation import validate_customer_frame


def test_validate_and_build_features():
    rows = load_customer_data("data/raw/customers.csv")
    records = validate_customer_frame(rows)
    features = build_features(rows)
    assert len(records) == len(rows)
    assert "income_per_tenure" in features[0]
    assert "plan_type_enterprise" in features[0]
