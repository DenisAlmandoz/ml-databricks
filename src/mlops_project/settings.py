from pathlib import Path
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables or .env in real deployments."""

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")

    mlops_env: str = Field(default="local")
    databricks_host: AnyUrl | None = Field(default=None)
    databricks_token: str | None = Field(default=None)
    model_registry_uri: str = Field(default="models:/customer_value_model")
    alert_email: str = Field(default="mlops@example.com")
    project_root: Path = Path(__file__).resolve().parents[2]


def get_settings() -> Settings:
    return Settings()
