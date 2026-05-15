from mlops_project.training.metrics import classification_metrics


def evaluate_model(model: dict, rows: list[dict], y_true: list[int]) -> dict[str, float]:
    probabilities = [score_row(model, row) for row in rows]
    predictions = [int(probability >= 0.5) for probability in probabilities]
    return classification_metrics(y_true, predictions, probabilities)


def score_row(model: dict, row: dict) -> float:
    spend = float(row["monthly_spend"])
    income = float(row["annual_income"])
    raw = 0.7 * (spend / model["spend_threshold"]) + 0.3 * (income / model["income_threshold"])
    return max(0.0, min(1.0, raw / 2))
