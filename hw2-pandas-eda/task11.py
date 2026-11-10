"""
Задание 11*. Окупаемость маркетинга по неделям.

Маркетологи ведут затраты в JSON (data/marketing.json): список записей вида
{"week": "2010-03-01", "spend": {"email": 182.34, "search": 1235.45}, "manager": "Ann"},
где week - понедельник недели, spend - затраты в фунтах по каналам. Канала без затрат в неделе
нет в словаре, недели без затрат нет в списке.
"""

from pathlib import Path

import pandas as pd


def load_marketing(path: str | Path) -> pd.DataFrame:
    """
    Прочитайте файл затрат. Верните DataFrame в «длинном» виде со столбцами week (datetime64),
    channel (str), spend (float): одна строка - одна пара «неделя, канал» с затратами. Порядок -
    по week, внутри недели - по channel.
    """
    # TODO: ваш код здесь
    ...


def weekly_romi(sales: pd.DataFrame, marketing: pd.DataFrame) -> pd.DataFrame:
    """
    Посчитайте по неделям продаж (как в weekly_revenue из задания 8) выручку, суммарные затраты
    на маркетинг (marketing - результат load_marketing) и ROMI = (выручка - затраты) / затраты.
    Верните DataFrame: индекс - понедельник недели, столбцы revenue, spend, romi. Недели - ровно
    те, что в weekly_revenue; в неделях без затрат spend = 0, romi = NaN.
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
