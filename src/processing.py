from typing import List, Dict, Any

def filter_by_state(data_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список по состоянию"""
    return [item for item in data_list if item.get("state") == state]

def sort_by_date(sort_data_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список по дате, предполагая, что 'date' всегда есть и сравним"""
    return sorted(
        sort_data_list,
        key=lambda x: x.get("date") or "",
        reverse=descending
    )