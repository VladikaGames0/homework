import pytest
from src.masks import get_mask_account,get_mask_card_number


@pytest.mark.parametrize("input_val", [
    "12345",
    "",
    "1234567890",
])

def test_edge_cases(input_val):
    """Проверяем что функция не падает и возвращает корректный формат"""
    result = get_mask_card_number(input_val)
    # Длина результата должна быть (len(input) при длине ≤10, но функция не рассчитана на это)
    assert isinstance(result, str)
    assert all(c.isdigit() or c == "*" or c == " " for c in result)


@pytest.mark.parametrize("input_val, expected", [("", "** "),
    ])
def test_get_mask_account(input_val, expected):
    """Если пустая строка, то  — возвращает '**'"""
    assert get_mask_account(input_val) == expected