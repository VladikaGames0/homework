from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.fixture
def empty_list():
    """Фикстура возвращает пустой список"""
    return []


def test_filter_empty_list(empty_list) -> None:
    """Проверяет пустой список"""
    assert filter_by_state(empty_list) == []


def test_sort_empty_list(empty_list) -> None:
    """Проверяет пустой список"""
    assert sort_by_date(empty_list, descending=True) == []
