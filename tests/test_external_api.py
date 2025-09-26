import unittest
from unittest.mock import patch, Mock
from external_api import convert_to_rub

class TestConvertToRub(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_rub_currency_returns_same_amount(self, mock_get):
        # Для RUB не вызывается API
        result = convert_to_rub(100.0, "RUB")
        self.assertEqual(result, 100.0)
        mock_get.assert_not_called()

    @patch('external_api.requests.get')
    def test_unsupported_currency_returns_same_amount(self, mock_get):
        # Для валют, кроме USD, EUR, RUB возвращаем тот же amount
        result = convert_to_rub(50.0, "JPY")
        self.assertEqual(result, 50.0)
        mock_get.assert_not_called()


    @patch('external_api.requests.get')
    def test_successful_eur_conversion(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "rates": {"RUB": 90.0}
        }
        mock_get.return_value = mock_response

        result = convert_to_rub(3.0, "EUR")
        self.assertAlmostEqual(result, 270.0)

    @patch('external_api.requests.get')
    def test_api_raises_exception_returns_amount(self, mock_get):
        mock_get.side_effect = Exception("API failure")

        result = convert_to_rub(10.0, "USD")
        self.assertEqual(result, 10.0)

    @patch('external_api.requests.get')
    def test_missing_rub_rate_returns_amount(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "rates": {}
        }
        mock_get.return_value = mock_response

        result = convert_to_rub(20.0, "USD")
        self.assertEqual(result, 20.0)

if __name__ == "__main__":
    unittest.main()
