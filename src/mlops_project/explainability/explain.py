def top_linear_coefficients(model: dict, top_n: int = 5) -> list[tuple[str, float]]:
    """Simple explainability helper for the threshold baseline."""
    weights = [("monthly_spend", 0.7), ("annual_income", 0.3)]
    return weights[:top_n]
