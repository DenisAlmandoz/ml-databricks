from dataclasses import dataclass


@dataclass
class Alert:
    severity: str
    message: str
    destination: str


def build_drift_alert(metric_name: str, value: float, threshold: float, destination: str) -> Alert | None:
    if value <= threshold:
        return None
    return Alert("warning", f"{metric_name} drift {value:.3f} exceeded threshold {threshold:.3f}", destination)
