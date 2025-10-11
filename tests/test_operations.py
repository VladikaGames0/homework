import pytest
from src.operations import process_bank_operations

@pytest.fixture
def sample_data():
    return [
        {'description': 'Оплата ЖКХ'},
        {'description': 'Оплата интернета'},
        {'description': 'Перевод родственникам'},
        {'description': 'Оплата ЖКХ и прочее'},
        {'description': None},
        {},
    ]

def test_process_bank_operations_count(sample_data):
    categories = ['Оплата', 'Перевод', 'Покупка']
    result = process_bank_operations(sample_data, categories)
    assert result['Оплата'] == 3  # три операции с "Оплата" в описании
    assert result['Перевод'] == 1
    assert result['Покупка'] == 0

def test_process_bank_operations_empty_categories(sample_data):
    result = process_bank_operations(sample_data, [])
    assert result == {}

def test_process_bank_operations_empty_data():
    result = process_bank_operations([], ['Оплата'])
    assert result == {'Оплата': 0}
