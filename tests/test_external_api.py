import unittest
from unittest.mock import patch, Mock
import os
from src.external_api import convert_to_rub

class TestExternalAPI(unittest.TestCase):

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_to_rub_usd(self, mock_get, mock_getenv):
        # Мокируем переменные окружения и ответ API
        mock_getenv.return_value = 'test_api_key'
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'RUB': 75.0}}
        mock_get.return_value = mock_response
        mock_response.raise_for_status.return_value = None
        transaction = {'operationAmount': {'amount': '100', 'currency': {'code': 'USD'}}}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_to_rub_rub(self, mock_get, mock_getenv):
        # Мокируем ситуацию, когда валюта уже в рублях
        mock_getenv.return_value = 'test_api_key'
        transaction = {'operationAmount': {'amount': '100', 'currency': {'code': 'RUB'}}}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_to_rub_api_error(self, mock_get, mock_getenv):
        # Мокируем ошибку от API
        mock_getenv.return_value = 'test_api_key'
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_get.return_value = mock_response

        transaction = {'operationAmount': {'amount': '100', 'currency': {'code': 'USD'}}}
        with self.assertRaises(Exception) as context:
            convert_to_rub(transaction)
        self.assertEqual(str(context.exception), "API Error")
