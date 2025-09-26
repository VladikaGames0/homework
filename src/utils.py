import json
from typing import List, Dict

def load_transactions(file_path: str) -> List[Dict]:
    """Загружает данные из JSON-файла с финансовыми транзакциями."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []