import os
from pydantic import BaseModel


class BaseSettings(BaseModel):
    def __init__(self, **data):
        annotations = getattr(self, "__annotations__", {})
        merged = dict(data)
        for name in annotations:
            env_name = name.upper()
            if name not in merged and env_name in os.environ:
                merged[name] = os.environ[env_name]
        super().__init__(**merged)


SettingsConfigDict = dict
