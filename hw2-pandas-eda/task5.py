"""
Задание 5. Смесь валют.

С июля часть счетов выставляется не в фунтах: в столбце currency встречаются GBP, EUR и USD,
а price указан в валюте счёта. Курсы лежат в таблице fx_rates (data/fx_rates.csv) со столбцами:
- date - дата (datetime64, без времени), курсы есть на каждый календарный день периода;
- currency - валюта (EUR, USD);
- units_per_gbp - сколько единиц валюты стоит 1 фунт в этот день.
"""

import pandas as pd


def to_gbp(orders: pd.DataFrame, fx_rates: pd.DataFrame) -> pd.DataFrame:
    """
    Переведите цены в фунты по курсу дня счёта. Верните копию orders с новым столбцом
    price_gbp - цена за штуку в фунтах. Число и порядок строк - как в orders, индекс тот же.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    from task1 import load_orders

    DATA = Path(__file__).parent / "data"
    orders = load_orders(DATA / "orders.csv")
    fx_rates = pd.read_csv(DATA / "fx_rates.csv", parse_dates=["date"])
    converted = to_gbp(orders, fx_rates)
    print(converted[converted["currency"] != "GBP"][["invoice", "price", "currency", "price_gbp"]].head())
