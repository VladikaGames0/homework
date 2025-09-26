def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.
    Возвращает генератор, который последовательно отдаёт только транзакции с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который по очереди возвращает строковое описание каждой транзакции.
    """
    for t in transactions:
        desc = f"Transaction of {t.get('amount', 'unknown')} {t.get('currency', '')} " \
               f"from {t.get('from', 'unknown')} to {t.get('to', 'unknown')}"
        yield desc


def card_number_generator(start, end):
    """
    Генератор банковских номеров карт в формате XXXX XXXX XXXX XXXX
    от start до end включительно (строковые значения, например "0000 0000 0000 0001").
    """
    start_num = int(start.replace(" ", ""))
    end_num = int(end.replace(" ", ""))

    for num in range(start_num, end_num + 1):
        card_str = f"{num:016d}"
        formatted = " ".join(card_str[i:i + 4] for i in range(0, 16, 4))
        yield formatted

transactions = [
    {"amount": 100, "currency": "USD", "from": "Alice", "to": "Bob"},
    {"amount": 50, "currency": "EUR", "from": "Carol", "to": "Dave"},
    {"amount": 70, "currency": "USD", "from": "Eve", "to": "Frank"},
]
