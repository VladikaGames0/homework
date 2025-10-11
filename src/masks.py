import logging
import os
from typing import Union

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "masks.log")
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure the directory exists

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Выводит только первые 6 и последние 4 цифры"""
    logger.info(f"Masking card number: {card_number}")
    s = str(card_number)
    masked = s[:6] + "*" * (len(s) - 10) + s[-4:]
    logger.debug(f"Masked card number: {masked}")
    return " ".join(masked[i : i + 4] for i in range(0, len(masked), 4))


def get_mask_account(last_card_number: Union[str, int]) -> str:
    """Выводит только последние 4 цифры"""
    logger.info(f"Masking account number: {last_card_number}")
    s = str(last_card_number)
    masked = f"** {s[-4:]}"
    logger.debug(f"Masked account number: {masked}")
    return masked

if __name__ == "main":
    card_number = "1234567890123456"
    account_number = "9876543210"

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print(f"Masked Card: {masked_card}")
    print(f"Masked Account: {masked_account}")