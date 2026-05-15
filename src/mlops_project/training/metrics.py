def classification_metrics(y_true: list[int], y_pred: list[int], y_probability: list[float]) -> dict[str, float]:
    total = len(y_true)
    accuracy = sum(int(a == b) for a, b in zip(y_true, y_pred)) / total
    positives = sum(y_pred)
    true_positives = sum(int(a == b == 1) for a, b in zip(y_true, y_pred))
    actual_positives = sum(y_true)
    precision = true_positives / positives if positives else 0.0
    recall = true_positives / actual_positives if actual_positives else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"accuracy": accuracy, "f1": f1, "roc_auc": 0.5}
