import pytest
from src.search import process_bank_search

@pytest.fixture
def sample_data():
    return [
        {'description': 'Перевод на карту', 'other_field': 1},
        {'description': 'Оплата услуг', 'other_field': 2},
        {'description': 'Перевод средств клиенту', 'other_field': 3},
        {'description': None},
        {'other_field': 5},
    ]

def test_process_bank_search_basic(sample_data):
    result = process_bank_search(sample_data, 'перевод')
    assert len(result) == 2
    descs = [item['description'].lower() for item in result]
    assert 'перевод на карту' in descs
    assert 'перевод средств клиенту' in descs

def test_process_bank_search_case_insensitive(sample_data):
    result_upper = process_bank_search(sample_data, 'ПЕРЕВОД')
    result_lower = process_bank_search(sample_data, 'перевод')
    assert result_upper == result_lower

def test_process_bank_search_no_matches(sample_data):
    result = process_bank_search(sample_data, 'не найдено')
    assert result == []

def test_process_bank_search_empty_string(sample_data):
    result = process_bank_search(sample_data, '')
    filtered = [item for item in sample_data if item.get('description')]
    assert result == filtered
