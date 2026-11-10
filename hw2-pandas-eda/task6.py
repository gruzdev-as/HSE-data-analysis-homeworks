"""
Задание 6. Выручка по странам и месяцам.

Работаете с чистыми продажами sales (пример - data/sales.csv): дубли, тестовые аккаунты и
отмены уже удалены, цены переведены в фунты, страны приведены к единому виду. Столбцы:
invoice, stock_code, description, quantity, invoice_date (datetime64), price (фунты),
customer_id (Int64, пусто у гостей), country. Выручка строки - quantity * price.
"""

import pandas as pd


def revenue_by_country(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте выручку по странам. Верните Series: индекс - страна, значения - выручка,
    по убыванию, при равенстве - по алфавиту.
    """
    # TODO: ваш код здесь
    ...


def monthly_pivot(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Постройте таблицу выручки «страна × месяц»: строки - страны по алфавиту, столбцы - месяцы
    в виде строк "ГГГГ-ММ" по порядку, от первого до последнего месяца в sales без пропусков.
    Если в стране в каком-то месяце продаж не было, поставьте 0.
    """
    # TODO: ваш код здесь
    ...


def average_order_value(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте средний чек по странам: средняя сумма одного счёта. Верните Series: индекс -
    страна (по алфавиту), значения - средний чек.
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
    print(monthly_pivot(sales).iloc[:5, :6])
    print(average_order_value(sales).head())
