def cap_outliers(rows: list[dict], column: str, upper_value: float) -> list[dict]:
    result = []
    for row in rows:
        item = dict(row)
        item[column] = min(float(item[column]), upper_value)
        result.append(item)
    return result
