import re
from typing import List, Dict

def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет операции в списке словарей по заданной строке в поле description с помощью регулярных выражений.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    filtered = [item for item in data if item.get('description') and pattern.search(item['description'])]
    return filtered
