from pydantic import ValidationError
from mlops_project.schemas import CustomerRecord


def validate_customer_frame(rows: list[dict]) -> list[CustomerRecord]:
    records: list[CustomerRecord] = []
    errors: list[str] = []
    seen: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        try:
            record = CustomerRecord(**row)
            if record.customer_id in seen:
                raise ValidationError("customer_id must be unique")
            seen.add(record.customer_id)
            records.append(record)
        except Exception as exc:
            errors.append(f"row {row_number}: {exc}")
    if errors:
        raise ValueError("Customer data contract violations:\n" + "\n".join(errors))
    return records
