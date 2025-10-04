import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")

def convert_to_rub(transaction):
    """Конвертирует сумму транзакции в рубли, если валюта отличается от RUB."""
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return float(amount)
    elif currency in ('USD', 'EUR'):
        exchange_rate = get_exchange_rate(currency)
        if exchange_rate:
            return float(amount) * exchange_rate
        else:
            return None

def get_exchange_rate(currency):
    """Получает текущий курс валюты к рублю через API."""
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}'
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['rates']['RUB']
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None