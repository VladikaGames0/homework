import pytest
from src.processing import filter_by_state,sort_by_date

def test_filter_empty_list():
    """Проверяет пустой список"""
    assert filter_by_state([]) == []


def test_sort_empty_list():
    """Проверяет пустой список"""
    assert sort_by_date([], descending=True) == []

