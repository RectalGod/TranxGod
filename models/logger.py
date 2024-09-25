import logging
from pathlib import Path
from typing import Optional
from models.config import LOG_SUCCESS_MESSAGE, LOG_FAILURE_MESSAGE

def setup_logging(log_level: str) -> None:
    logging.basicConfig(level=log_level, format='%(message)s')
    logging.getLogger("urllib3").setLevel(logging.WARNING)

def log_translation(file_path: Path, status: str, error: Optional[Exception] = None) -> None:
    if status == "success":
        logging.info(LOG_SUCCESS_MESSAGE.format(file_path=file_path))
    elif status == "failure":
        logging.error(LOG_FAILURE_MESSAGE.format(file_path=file_path, error=error))
