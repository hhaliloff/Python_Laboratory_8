import os
import sys
import unittest
from unittest.mock import patch

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# добавляем utils в путь
UTILS_DIR = os.path.join(PROJECT_ROOT, "utils")
if UTILS_DIR not in sys.path:
    sys.path.insert(0, UTILS_DIR)

import currencies_api
from currencies_api import get_currencies


class TestGetCurrencies(unittest.TestCase):

    @patch("currencies_api.requests.get")
    def test_get_currencies_success(self, mock_get):
        """Успешное получение валют."""
        mock_get.return_value.status_code = 200
        # Структура такая же, как у реального API:
        # data["Valute"][<код>]["Value"]
        mock_get.return_value.json.return_value = {
            "Valute": {
                "USD": {"Value": 90.0},
                "EUR": {"Value": 100.0},
            }
        }

        result = get_currencies(["USD", "EUR"])

        self.assertIsInstance(result, dict)
        self.assertEqual(result["USD"], 90.0)
        self.assertEqual(result["EUR"], 100.0)

    @patch("currencies_api.requests.get")
    def test_get_currencies_network_error(self, mock_get):
        """Ошибка сети — должно быть исключение."""
        mock_get.side_effect = Exception("Network error")

        with self.assertRaises(Exception):
            get_currencies(["USD"])

    @patch("currencies_api.requests.get")
    def test_get_currencies_invalid_json(self, mock_get):
        """Некорректный JSON — должно быть исключение."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = ValueError("Invalid JSON")

        with self.assertRaises(Exception):
            get_currencies(["USD"])

    @patch("currencies_api.requests.get")
    def test_get_currencies_no_rates(self, mock_get):
        """Отсутствует ключ 'Valute' или нужная валюта — должно быть исключение."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}

        with self.assertRaises(Exception):
            get_currencies(["USD"])


if __name__ == "__main__":
    unittest.main()
