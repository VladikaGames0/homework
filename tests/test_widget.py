import pytest
from src.widget import mask_account_card,get_date

@pytest.mark.parametrize("input_val, expected", [
    ("Счет 123", "Счет **123"),
])
def test_mask_account_card(input_val, expected):
    """Проверяем, если счёт меньше 4 символов"""
    assert mask_account_card(input_val) == expected

def test_get_date_no_time():
    """Проверяем, если нет времени"""
    assert get_date("2024-06-24") == "24.06.2024"