"""Tiny educational subset of Pydantic used for offline fundamentals tests.

Install real `pydantic` in production; this shim exists so the sample project can
run in restricted training environments without downloading packages.
"""

class ValidationError(ValueError):
    pass


def Field(default=None, **_kwargs):
    return default


def field_validator(*_fields):
    def decorator(func):
        return func
    return decorator


AnyUrl = str
SettingsConfigDict = dict


class BaseModel:
    def __init__(self, **data):
        annotations = getattr(self.__class__, "__annotations__", {})
        for name in annotations:
            if name in data:
                setattr(self, name, data[name])
            elif hasattr(self.__class__, name):
                setattr(self, name, getattr(self.__class__, name))
            else:
                raise ValidationError(f"missing required field: {name}")

    def model_dump(self):
        return dict(self.__dict__)
