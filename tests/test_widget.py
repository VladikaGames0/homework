import pytest
from src.widget import mask_account_card, get_date
from typing import Union


@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("Счет 123", "Счет **123"),
    ],
)
def test_mask_account_card(input_val: str, expected: str) -> None:
    """Проверяем, если счёт меньше 4 символов"""
    assert mask_account_card(input_val) == expected


def test_get_date_no_time() -> None:
    """Проверяем, если нет времени"""
    assert get_date("2024-06-24") == "24.06.2024"


def test_mask_account_card_without_schet() -> None:
    """Проверяет, если не написанно 'Счет'"""
    assert mask_account_card("Visa 1234567812345678") == "Visa 1234567812345678"
    assert mask_account_card(1234567890) == "1234567890"
