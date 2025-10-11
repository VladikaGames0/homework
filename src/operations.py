from collections import Counter
from typing import List, Dict

def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям на основе наличия категории в поле description.
    """
    counter = Counter()
    for category in categories:
        count = sum(
            1 for item in data if item.get('description') and category.lower() in item['description'].lower()
        )
        counter[category] = count
    return dict(counter)
