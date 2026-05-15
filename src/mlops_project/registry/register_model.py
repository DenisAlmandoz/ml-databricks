from dataclasses import dataclass


@dataclass
class RegisteredModel:
    name: str
    version: str
    stage: str


def register_model(model_name: str, artifact_path: str, stage: str = "Staging") -> RegisteredModel:
    """Placeholder for MLflow/Databricks Model Registry registration."""
    return RegisteredModel(name=model_name, version=f"local:{artifact_path}", stage=stage)
