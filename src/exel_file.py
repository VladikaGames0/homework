from pathlib import Path
import pandas as pd

filepath_xlsx = Path("..", "data", "transactions_excel.xlsx")


def read_excel_file(excel_file_path):
    """
    Считывает финансовые операции из excel-файла.
    """
    try:
        reader = pd.read_excel(excel_file_path)
        dict_list = reader.to_dict(orient="records")
        return dict_list

    except FileNotFoundError:

        raise FileNotFoundError("No such file or directory")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        raise

print(read_excel_file(filepath_xlsx))
