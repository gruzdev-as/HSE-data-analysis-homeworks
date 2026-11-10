"""
Задание 10*. Курс последнего рабочего дня.

Банк публикует курсы только по рабочим дням (data/fx_rates_business.csv, столбцы как в
задании 5: date, currency, units_per_gbp), а магазин продаёт и в выходные.
"""

import pandas as pd


def to_gbp_asof(orders: pd.DataFrame, fx_rates: pd.DataFrame) -> pd.DataFrame:
    """
    Переведите цены в фунты, как в задании 5, но по последнему опубликованному курсу на дату
    счёта (в тот же день или раньше). Если такого курса нет - NaN. Верните копию orders с новым
    столбцом price_gbp, число и порядок строк - как в orders, индекс тот же.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    from task1 import load_orders

    DATA = Path(__file__).parent / "data"
    orders = load_orders(DATA / "orders.csv")
    fx_rates = pd.read_csv(DATA / "fx_rates_business.csv", parse_dates=["date"])
    converted = to_gbp_asof(orders, fx_rates)
    weekend = converted["invoice_date"].dt.day_of_week >= 5
    print(converted[weekend & (converted["currency"] != "GBP")][["invoice", "price", "currency", "price_gbp"]].head())
