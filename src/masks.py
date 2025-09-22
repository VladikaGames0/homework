from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """ "Выводит только первые 6 и последние 4 цифры"""
    s = str(card_number)
    masked = s[:6] + "*" * (len(s) - 10) + s[-4:]
    return " ".join(masked[i : i + 4] for i in range(0, len(masked), 4))


def get_mask_account(last_card_number: Union[str, int]) -> str:
    """ "Выводит только последние 4 цифры"""
    s = str(last_card_number)
    return f"** {s[-4:]}"
