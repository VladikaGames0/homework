import json
import logging
from typing import List, Dict

logger = logging.getLogger("utils")

def load_transactions(file_path: str) -> List[Dict]:
    """Загружает данные из JSON-файла с финансовыми транзакциями."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            logger.info(f"Успешно загружены транзакции из файла: {file_path}")
            return data
        else:
            logger.warning(f"Данные в файле {file_path} имеют неверный формат (не список).")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON из файла: {file_path}")
        return []
