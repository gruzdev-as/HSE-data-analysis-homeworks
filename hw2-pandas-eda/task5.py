"""
Задание 5. Отчёт по странам.

Работаете с чистыми продажами sales (столбцы - как в задании 3, пример - data/sales.csv).
Выручка строки - quantity * price.
"""

import pandas as pd


def monthly_pivot(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Постройте таблицу выручки «страна × месяц»: строки - страны по алфавиту, столбцы - месяцы
    в виде строк "ГГГГ-ММ" по порядку, от первого до последнего месяца в sales без пропусков.
    Если в стране в каком-то месяце продаж не было, поставьте 0.

    Пример: продажи France в 2010-11 на 40 и в 2011-01 на 20 -> столбцы
    "2010-11", "2010-12", "2011-01", строка France: 40, 0, 20.
    """
    # TODO: ваш код здесь
    ...


def country_report(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Соберите отчёт по странам. Верните DataFrame: индекс - страна, строки по убыванию выручки,
    при равенстве - по алфавиту; столбцы:
        "revenue" - выручка;
        "invoices" - число счетов;
        "buyers" - число разных клиентов (гостевые продажи - не клиенты);
        "aov" - средний чек, средняя сумма одного счёта;
        "best_month" - месяц "ГГГГ-ММ" с наибольшей выручкой в стране (как в monthly_pivot),
            при равенстве - более ранний.

    Пример: в Spain два счёта клиента 7 на 100 и 300 в 2010-11 и 2010-12 -> revenue 400,
    invoices 2, buyers 1, aov 200, best_month "2010-12".
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
    print(monthly_pivot(sales).iloc[:5, :6])
    print(country_report(sales).head(10))
