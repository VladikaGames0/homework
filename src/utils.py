import json
import os

def load_transactions(filepath):
    """Загружает данные о транзакциях из JSON-файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
