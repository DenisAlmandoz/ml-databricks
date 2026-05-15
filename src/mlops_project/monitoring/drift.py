def mean_drift(reference: list[dict], current: list[dict], column: str) -> float:
    reference_mean = sum(float(row[column]) for row in reference) / len(reference)
    current_mean = sum(float(row[column]) for row in current) / len(current)
    if reference_mean == 0:
        return 0.0 if current_mean == 0 else 1.0
    return abs(current_mean - reference_mean) / abs(reference_mean)
