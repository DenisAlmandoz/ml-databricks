import json
from mlops_project.features.feature_engineering import build_features
from mlops_project.schemas import PredictionResponse
from mlops_project.training.evaluate import score_row
from mlops_project.utils.paths import resolve_path


def predict_records(model_path: str, records: list[dict]) -> list[PredictionResponse]:
    model = json.loads(resolve_path(model_path).read_text())
    rows = [dict(record, high_value=record.get("high_value", 0)) for record in records]
    features = build_features(rows)
    responses = []
    for row in features:
        probability = score_row(model, row)
        responses.append(PredictionResponse(
            customer_id=row["customer_id"],
            high_value_probability=probability,
            predicted_high_value=int(probability >= 0.5),
        ))
    return responses
