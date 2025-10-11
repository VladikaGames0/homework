import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions
import json

class TestUtils(unittest.TestCase):

    def test_load_transactions_success(self):
        # Мокируем содержимое файла
        mock_data = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            result = load_transactions("fake_path.json")
            self.assertEqual(result, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    def test_load_transactions_empty_file(self):
        with patch("builtins.open", mock_open(read_data='')) as mock_file:
            result = load_transactions("fake_path.json")
            self.assertEqual(result, [])

    def test_load_transactions_invalid_json(self):
        with patch("builtins.open", mock_open(read_data='invalid json')) as mock_file:
            result = load_transactions("fake_path.json")
            self.assertEqual(result, [])

    def test_load_transactions_not_a_list(self):
        mock_data = '{"key": "value"}'
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            result = load_transactions("fake_path.json")
            self.assertEqual(result, [])

    def test_load_transactions_file_not_found(self):
        with patch("builtins.open") as mocked_open:
            mocked_open.side_effect = FileNotFoundError
            result = load_transactions("non_existent_file.json")
            self.assertEqual(result, [])