"""
Задание 10*. Окупаемость маркетинга по неделям.

Маркетологи ведут затраты в JSON (data/marketing.json): список записей вида
{"week": "2010-03-01", "spend": {"email": 182.34, "search": 1235.45}, "manager": "Ann"},
где week - понедельник недели, spend - затраты в фунтах по каналам. Канала без затрат в неделе
нет в словаре, недели без затрат нет в списке. Продажи sales - как в задании 3.
"""

from pathlib import Path

import pandas as pd


def load_marketing(path: str | Path) -> pd.DataFrame:
    """
    Прочитайте файл затрат. Верните DataFrame в «длинном» виде со столбцами week (datetime64),
    channel (str), spend (float): одна строка - одна пара «неделя, канал» с затратами. Порядок -
    по week, внутри недели - по channel.

    Пример: [{"week": "2010-03-01", "spend": {"search": 100.0, "email": 10.0}, "manager": "Ann"}] ->
    две строки: (2010-03-01, "email", 10.0), (2010-03-01, "search", 100.0).
    """
    # TODO: ваш код здесь
    ...


def weekly_romi(sales: pd.DataFrame, marketing: pd.DataFrame) -> pd.DataFrame:
    """
    Посчитайте по неделям (с понедельника по воскресенье) выручку, суммарные затраты на
    маркетинг (marketing - результат load_marketing) и ROMI = (выручка - затраты) / затраты.
    Верните DataFrame: индекс - понедельник недели, все недели от первой до последней недели
    в sales по порядку; столбцы revenue, spend, romi. В неделях без продаж revenue = 0,
    в неделях без затрат spend = 0, romi = NaN.

    Пример: неделя 2010-03-01 - выручка 300, затраты 100 -> romi 2.0.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    DATA = Path(__file__).parent / "data"
    sales = pd.read_csv(
        DATA / "sales.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date"],
    )
    marketing = load_marketing(DATA / "marketing.json")
    print(marketing.head())
    print(weekly_romi(sales, marketing).tail(12))
