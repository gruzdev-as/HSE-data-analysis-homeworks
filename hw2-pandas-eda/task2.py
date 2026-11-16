"""
Задание 2. Страны и отмены.

Работаете с выгрузкой заказов orders (столбцы - как в задании 1, invoice_date - datetime64,
customer_id - Int64). Страну в заказ вписывают вручную, поэтому одна и та же страна записана
по-разному. Функции не должны менять переданные данные.
"""

import pandas as pd

COUNTRY_ALIASES = {
    "UK": "United Kingdom",
    "U.K.": "United Kingdom",
    "EIRE": "Ireland",
    "USA": "United States",
    "RSA": "South Africa",
}


def normalize_country(countries: pd.Series) -> pd.Series:
    """
    Приведите названия стран к единому виду:
    - сравнение без учёта регистра и пробелов в начале и конце;
    - названия из COUNTRY_ALIASES (ключи) замените на значения словаря;
    - остальные запишите с заглавной буквы в каждом слове: "united kingdom" -> "United Kingdom";
    - пропуски оставьте пропусками.
    Верните Series той же длины и с тем же индексом.

    Пример:
        normalize_country(pd.Series(["France", "EIRE", "hong kong"])) -> ["France", "Ireland", "Hong Kong"]
    """
    # TODO: ваш код здесь
    ...


def customers_by_country(orders: pd.DataFrame) -> pd.Series:
    """
    Посчитайте число разных клиентов в каждой стране (после приведения названий, как в
    normalize_country). Гостевые заказы (без customer_id) не учитывайте; страны, где были
    только гостевые заказы, в результат не включайте. Верните Series: индекс - страна,
    значения - число клиентов, по убыванию, при равенстве - по алфавиту.

    Пример: клиенты 1 и 2 из "France", клиент 3 из "Spain" -> France 2, Spain 1.
    """
    # TODO: ваш код здесь
    ...


def split_cancellations(orders: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Разделите строки на обычные и отмены. Отмена - строка, номер счёта которой начинается
    с буквы C. Верните пару (обычные строки, отмены), порядок строк внутри каждой части -
    как в orders.

    Пример: счета "536365", "C536379", "536380" -> (["536365", "536380"], ["C536379"]).
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    orders = pd.read_csv(
        Path(__file__).parent / "data" / "orders_iso.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date", "loaded_at"],
    )
    print("Было:", sorted(orders["country"].dropna().unique()))
    print("Стало:", sorted(normalize_country(orders["country"]).dropna().unique()))
    print(customers_by_country(orders).head(10))
    regular, cancellations = split_cancellations(orders)
    print("Обычных строк:", len(regular), "отмен:", len(cancellations))
