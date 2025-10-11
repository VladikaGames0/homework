import json
import logging
import os

# Настройка логирования
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "utils.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",  # Перезапись лог-файла при каждом запуске
)

logger = logging.getLogger(__name__)


def load_transactions(filepath):
    """Загружает данные о транзакциях из JSON-файла."""
    logger.info(f"Loading transactions from file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Successfully loaded {len(data)} transactions.")
                return data
            else:
                logger.warning("Data in file is not a list. Returning empty list.")
                return []
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSONDecodeError: Could not decode file {filepath}")
        return []

