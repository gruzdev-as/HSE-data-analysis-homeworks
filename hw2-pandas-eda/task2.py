"""
Задание 2. Выборки и топ товаров.

Работаете с выгрузкой заказов orders в том виде, как её возвращает load_orders из задания 1
(invoice_date - datetime64, customer_id - Int64). Товар определяется кодом stock_code.
Функции не должны менять переданный DataFrame.
"""

import pandas as pd


def add_line_total(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Верните копию orders с новым столбцом line_total - сумма строки (quantity * price).
    """
    # TODO: ваш код здесь
    ...


def orders_in_period(orders: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """
    Верните строки, у которых дата счёта лежит в периоде с start по end включительно.
    start и end - даты в формате "ГГГГ-ММ-ДД". Порядок строк - как в orders.
    """
    # TODO: ваш код здесь
    ...


def top_products(orders: pd.DataFrame, n: int) -> pd.Series:
    """
    Найдите n товаров с наибольшей выручкой (сумма quantity * price по всем строкам товара).
    Верните Series: индекс - stock_code, значения - выручка, по убыванию выручки,
    при равенстве - по возрастанию stock_code. Если товаров меньше n - верните все.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    from task1 import load_orders

    orders = load_orders(Path(__file__).parent / "data" / "orders.csv")
    print(add_line_total(orders).head())
    print("Строк за декабрь 2010:", len(orders_in_period(orders, "2010-12-01", "2010-12-31")))
    print(top_products(orders, 5))
