from utils import load_transactions
from external_api import convert_to_rub

def main():
    file_path = 'data/operations.json'
    transactions = load_transactions(file_path)

    if transactions:
        for transaction in transactions:
            rub_amount = convert_to_rub(transaction)
            if rub_amount is not None:
                print(f"Сумма в рублях: {rub_amount}")
            else:
                print(f"Не удалось конвертировать транзакцию: {transaction}")
    else:
        print("Нет данных о транзакциях.")

if __name__ == "__main__":
    main()
