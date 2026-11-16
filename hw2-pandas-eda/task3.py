"""
Задание 3. Группировки.

Работаете с чистыми продажами sales (пример - data/sales.csv): дубли, тестовые аккаунты и
отмены уже удалены, цены переведены в фунты, страны приведены к единому виду. Столбцы:
invoice, stock_code, description, quantity, invoice_date (datetime64), price (фунты),
customer_id (Int64, пусто у гостей), country. Выручка строки - quantity * price.
Товар определяется кодом stock_code.
"""

import pandas as pd


def revenue_by_country(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте выручку по странам. Верните Series: индекс - страна, значения - выручка,
    по убыванию, при равенстве - по алфавиту.

    Пример: France - строки на 10 и 5, Spain - на 20 -> Spain 20, France 15.
    """
    # TODO: ваш код здесь
    ...


def top_products(sales: pd.DataFrame, n: int) -> pd.Series:
    """
    Найдите n товаров с наибольшей выручкой. Верните Series: индекс - stock_code, значения -
    выручка, по убыванию выручки, при равенстве - по возрастанию stock_code. Если товаров
    меньше n - верните все.

    Пример: товар "A" продан на 50, "B" на 120, "C" на 60 -> top_products(sales, 2) -> B 120, C 60.
    """
    # TODO: ваш код здесь
    ...


def average_order_value(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте средний чек по странам: средняя сумма одного счёта. Верните Series: индекс -
    страна (по алфавиту), значения - средний чек.

    Пример: в Spain два счёта на 100 и 300 -> Spain 200.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    sales = pd.read_csv(
        Path(__file__).parent / "data" / "sales.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date"],
    )
    print(revenue_by_country(sales).head())
    print(top_products(sales, 5))
    print(average_order_value(sales).head())
