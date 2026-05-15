FEATURE_COLUMNS = [
    "age",
    "annual_income",
    "tenure_months",
    "monthly_spend",
    "support_tickets",
    "plan_type_enterprise",
    "plan_type_pro",
    "income_per_tenure",
    "spend_per_ticket",
]


def build_features(rows: list[dict]) -> list[dict]:
    features: list[dict] = []
    for row in rows:
        tenure = int(row["tenure_months"])
        tickets = int(row["support_tickets"])
        plan_type = str(row["plan_type"])
        item = {
            "customer_id": row["customer_id"],
            "age": int(row["age"]),
            "annual_income": float(row["annual_income"]),
            "tenure_months": tenure,
            "monthly_spend": float(row["monthly_spend"]),
            "support_tickets": tickets,
            "plan_type_enterprise": int(plan_type == "enterprise"),
            "plan_type_pro": int(plan_type == "pro"),
            "income_per_tenure": float(row["annual_income"]) / (tenure + 1),
            "spend_per_ticket": float(row["monthly_spend"]) / (tickets + 1),
            "high_value": int(row.get("high_value", 0)),
        }
        features.append(item)
    return features


def split_xy(feature_rows: list[dict], target_column: str = "high_value"):
    x = [{key: row[key] for key in FEATURE_COLUMNS} for row in feature_rows]
    y = [int(row[target_column]) for row in feature_rows]
    return x, y
