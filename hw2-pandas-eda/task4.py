"""
Задание 4. Названия стран.

Страну в заказ вписывают вручную, поэтому одна и та же страна записана по-разному.
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
    """
    # TODO: ваш код здесь
    ...


def customers_by_country(orders: pd.DataFrame) -> pd.Series:
    """
    Посчитайте число разных клиентов в каждой стране (после приведения названий, как в
    normalize_country). Гостевые заказы (без customer_id) не учитывайте. Верните Series:
    индекс - страна, значения - число клиентов, по убыванию, при равенстве - по алфавиту.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    from task1 import load_orders

    orders = load_orders(Path(__file__).parent / "data" / "orders.csv")
    print("Было:", sorted(orders["country"].dropna().unique()))
    print("Стало:", sorted(normalize_country(orders["country"]).dropna().unique()))
    print(customers_by_country(orders).head(10))
