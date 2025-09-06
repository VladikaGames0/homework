import pytest
from src.masks import get_mask_account, get_mask_card_number
from typing import Union

@pytest.fixture(params=["12345", "", "1234567890"])
def input_val_edge(request) -> Union[str, int]:
    """Фикстура для теста test_edge_cases"""
    return request.param

@pytest.fixture(params=[("", "** "), ("1234", "** 1234"), ("987654321", "** 4321")])
def input_val_expected(request) -> tuple[Union[str, int], str]:
    """Фикстура для теста test_get_mask_account"""
    return request.param

def test_edge_cases(input_val_edge: Union[str, int]) -> None:
    """Проверяет является ли результат строкой"""
    result = get_mask_card_number(input_val_edge)
    assert isinstance(result, str)


def test_get_mask_account(input_val_expected: tuple[Union[str, int], str]) -> None:
    """Сравнивает возвращаемое значение функции get_mask_account с ожидаемым"""
    input_val, expected = input_val_expected
    assert get_mask_account(input_val) == expected
