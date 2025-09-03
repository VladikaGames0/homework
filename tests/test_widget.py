import pytest
from src.widget import mask_account_card,get_date

@pytest.mark.parametrize("input_val, expected", [
    ("Счет 1234567890", "Счет **7890"),
])
def test_mask_account_card(input_val, expected):
    assert mask_account_card(input_val) == expected