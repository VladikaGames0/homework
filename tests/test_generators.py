import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    return [
        {"amount": 100, "currency": "USD", "from": "Alice", "to": "Bob"},
        {"amount": 50, "currency": "EUR", "from": "Carol", "to": "Dave"},
        {"amount": 70, "currency": "USD", "from": "Eve", "to": "Frank"},
        {"amount": 30, "currency": "JPY", "from": "Gary", "to": "Helen"},
    ]

def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["currency"] == "USD" for t in result)

def test_filter_by_currency_none(transactions):
    result = list(filter_by_currency(transactions, "GBP"))
    assert result == []

def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Transaction of 100 USD from Alice to Bob",
        "Transaction of 50 EUR from Carol to Dave",
        "Transaction of 70 USD from Eve to Frank",
        "Transaction of 30 JPY from Gary to Helen",
    ]
    assert descriptions == expected

def test_transaction_descriptions_missing_fields():
    incomplete = [{"amount": 10}]
    descriptions = list(transaction_descriptions(incomplete))
    assert descriptions[0] == "Transaction of 10  from unknown to unknown"

def test_card_number_generator_basic():
    result = list(card_number_generator("0000 0000 0000 0001", "0000 0000 0000 0003"))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
    assert result == expected

def test_card_number_generator_single():
    result = list(card_number_generator("1234 5678 9012 3456", "1234 5678 9012 3456"))
    assert result == ["1234 5678 9012 3456"]
