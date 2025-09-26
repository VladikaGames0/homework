
import unittest
import os
import json
from src.utils import load_transactions

class TestLoadTransactions(unittest.TestCase):
    TEST_FILE = "test_transactions.json"
    INVALID_FILE = "invalid.json"
    NOT_FOUND_FILE = "not_exist.json"

    def setUp(self):
        # Создаём корректный JSON-файл с транзакциями (список словарей)
        data = [
            {"amount": 100, "currency": "USD"},
            {"amount": 200, "currency": "EUR"}
        ]
        with open(self.TEST_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)

        # Создаём файл с неверным форматом (например, словарь вместо списка)
        with open(self.INVALID_FILE, "w", encoding="utf-8") as f:
            json.dump({"amount": 100}, f)

    def tearDown(self):
        # Удаляем созданные тестовые файлы
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)
        if os.path.exists(self.INVALID_FILE):
            os.remove(self.INVALID_FILE)

    def test_load_valid_file(self):
        result = load_transactions(self.TEST_FILE)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["currency"], "USD")

    def test_load_invalid_format(self):
        result = load_transactions(self.INVALID_FILE)
        self.assertEqual(result, [])

    def test_file_not_found(self):
        result = load_transactions(self.NOT_FOUND_FILE)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
