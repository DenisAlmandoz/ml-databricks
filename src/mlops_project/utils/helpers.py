import json
from pathlib import Path


def read_simple_yaml(path: str | Path) -> dict:
    """Read the flat key/value YAML used by this starter project."""
    result: dict[str, str | int | float] = {}
    for raw_line in Path(path).read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line or raw_line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"')
        if value == "":
            continue
        if value.replace(".", "", 1).isdigit():
            result[key] = float(value) if "." in value else int(value)
        else:
            result[key] = value
    return result


def read_yaml(path: str | Path) -> dict:
    return read_simple_yaml(path)


def write_json(path: str | Path, payload: dict) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2))
