"""
Задание 9*. Курс последнего рабочего дня.

Банк публикует курсы только по рабочим дням (data/fx_rates_business.csv, столбцы как в
задании 4: date, currency, units_per_gbp), а магазин продаёт и в выходные. Работаете с
выгрузкой orders (столбцы - как в задании 1).
"""

import pandas as pd


def to_gbp_asof(orders: pd.DataFrame, fx_rates: pd.DataFrame) -> pd.DataFrame:
    """
    Переведите цены в фунты по последнему опубликованному курсу на дату счёта (в тот же день
    или раньше). Если такого курса нет - NaN. GBP не пересчитывается. Верните копию orders с
    новым столбцом price_gbp, число и порядок строк - как в orders, индекс тот же.

    Пример: курс EUR опубликован в пятницу 2010-07-02 (1.2), счёт в воскресенье 2010-07-04 на
    12.0 EUR -> price_gbp 10.0.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    orders = pd.read_csv(
        DATA / "orders_iso.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date", "loaded_at"],
    )
    fx_rates = pd.read_csv(DATA / "fx_rates_business.csv", parse_dates=["date"])
    converted = to_gbp_asof(orders, fx_rates)
    weekend = converted["invoice_date"].dt.day_of_week >= 5
    print(converted[weekend & (converted["currency"] != "GBP")][["invoice", "price", "currency", "price_gbp"]].head())
