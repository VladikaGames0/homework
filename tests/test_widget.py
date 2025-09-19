import pytest
from src.widget import mask_account_card, get_date
from typing import Union


@pytest.fixture
def account_with_short_schet() -> str:
    return "Счет 123"

@pytest.fixture
def visa_card() -> str:
    return "Visa 1234567812345678"

@pytest.fixture
def numeric_account() -> int:
    return 1234567890

@pytest.fixture
def date_without_time() -> str:
    return "2024-06-24"

@pytest.mark.parametrize(
    "input_val, expected",
    [
        ("Счет 123", "Счет **123"),
    ],
)


def test_mask_account_card(input_val: str, expected: str) -> None:
    """Проверяем, если счёт меньше 4 символов"""
    assert mask_account_card(input_val) == expected


def test_get_date_no_time(date_without_time) -> None:
    """Проверяем, если нет времени"""
    assert get_date(date_without_time) == "24.06.2024"


def test_mask_account_card_without_schet(visa_card, numeric_account) -> None:
    """Проверяет, если не написанно 'Счет'"""
    assert mask_account_card(visa_card) == visa_card
    assert mask_account_card(numeric_account) == str(numeric_account)
