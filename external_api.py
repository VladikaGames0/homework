import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest"

def convert_to_rub(transaction: dict) -> float:
    """
    Функция принимает транзакцию (словарь с ключами 'amount' и 'currency')
    и возвращает сумму в рублях (float).
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency", "").upper()

    if not isinstance(amount, (int, float)) or not currency:
        return 0.0

    if currency == "RUB":
        return float(amount)

    if currency not in ("USD", "EUR"):
        return float(amount)

    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"].get("RUB")
        if rate:
            return float(amount) * float(rate)
    except Exception:
        pass

    return float(amount)
