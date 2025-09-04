from typing import Union


def mask_account_card(card_number: Union[str, int]) -> str:
    """Принимает значение карты и возвращает название с замаскированным номером"""

    s = str(card_number)
    if s.startswith("Счет"):
        card_name = "Счет"
        number = s[len(card_name):].strip()
        return f"{card_name} **{number[-4:]}"

    else:
        parts = s.split()
        card_name = " ".join(parts[:-1])
        number = parts[-1]
        masked = number[:6] + "*" * (len(number) - 10) + number[-4:]
        formatted_number = " ".join(masked[i: i + 4] for i in range(0, len(masked), 4))
        return f"{card_name} {formatted_number}"


def get_date(date_str: str) -> str:
    """Переводит один формат даты в другой"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
