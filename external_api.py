import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest"

def convert_to_rub(amount: float, currency: str) -> float:
    currency = currency.upper()
    if currency == "RUB":
        return amount
    if currency not in ("USD", "EUR"):
        return amount

    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"].get("RUB")
        if rate:
            return amount * rate
    except Exception:
        pass

    return amount
