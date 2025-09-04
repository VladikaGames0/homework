import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_val",
    [
        "12345",
        "",
        "1234567890",
    ],
)
def test_edge_cases(input_val: str) -> None:
    """Проверяем что функция не падает и возвращает корректный формат"""
    result = get_mask_card_number(input_val)
    assert isinstance(result, str)
    assert all(c.isdigit() or c == "*" or c == " " for c in result)


@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("", " "),
    ],
)
def test_get_mask_account(input_val: str, expected: str) -> None:
    """Если пустая строка, то  — возвращает ''"""
    assert get_mask_account(input_val) == expected
