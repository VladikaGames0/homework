from typing import Union


def mask_account_card(card_number: Union[str, int]) -> str:
    """Принимает значение карты и возвращает название с замаскированным номером"""

    s = str(card_number)
    if s.startswith("Счет"):
        card_name = "Счет"
        number = s[len(card_name) :].strip()
        return f"{card_name} **{number[-4:]}"
    # Можно расширить логику для других случаев, если нужно
    return s


def get_date(date_str: str) -> str:
    """Переводит один формат даты в другой"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
