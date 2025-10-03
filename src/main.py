from utils import load_transactions
from external_api import convert_to_rub

if __name__ == 'main':
    transactions = load_transactions('data/operations.json')
    if transactions:
        for transaction in transactions:
            rub_amount = convert_to_rub(transaction)
            if rub_amount:
                print(f"Сумма в рублях: {rub_amount}")
            else:
                print("Не удалось конвертировать валюту.")
    else:
        print("Нет данных о транзакциях.")