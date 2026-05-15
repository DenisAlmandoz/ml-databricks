import logging


def configure_logging(config_path: str = "configs/logging.yaml") -> None:
    logging.basicConfig(level=logging.INFO, format='{"level":"%(levelname)s","message":"%(message)s"}')
