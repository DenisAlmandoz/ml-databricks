from enum import Enum
from pydantic import BaseModel, Field, ValidationError


class PlanType(str, Enum):
    basic = "basic"
    pro = "pro"
    enterprise = "enterprise"


class CustomerRecord(BaseModel):
    customer_id: str = Field(default="")
    age: int = Field(default=0)
    annual_income: float = Field(default=0.0)
    tenure_months: int = Field(default=0)
    monthly_spend: float = Field(default=0.0)
    support_tickets: int = Field(default=0)
    plan_type: PlanType = Field(default=PlanType.basic)
    high_value: int = Field(default=0)

    def __init__(self, **data):
        self.customer_id = str(data.get("customer_id", "")).strip()
        self.age = int(data.get("age", 0))
        self.annual_income = float(data.get("annual_income", 0.0))
        self.tenure_months = int(data.get("tenure_months", 0))
        self.monthly_spend = float(data.get("monthly_spend", 0.0))
        self.support_tickets = int(data.get("support_tickets", 0))
        self.plan_type = PlanType(str(data.get("plan_type", PlanType.basic.value)))
        self.high_value = int(data.get("high_value", 0))
        if not self.customer_id:
            raise ValidationError("customer_id is required")
        if not 18 <= self.age <= 100:
            raise ValidationError("age must be between 18 and 100")
        if min(self.annual_income, self.tenure_months, self.monthly_spend, self.support_tickets) < 0:
            raise ValidationError("numeric values must be non-negative")
        if self.high_value not in (0, 1):
            raise ValidationError("high_value must be 0 or 1")


class FeatureRecord(BaseModel):
    customer_id: str
    age: int
    annual_income: float
    tenure_months: int
    monthly_spend: float
    support_tickets: int
    plan_type_enterprise: int
    plan_type_pro: int
    income_per_tenure: float
    spend_per_ticket: float


class PredictionRequest(BaseModel):
    records: list[CustomerRecord]


class PredictionResponse(BaseModel):
    customer_id: str
    high_value_probability: float
    predicted_high_value: int
