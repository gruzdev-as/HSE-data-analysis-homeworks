"""
Задание 8. Выручка во времени.

Работаете с чистыми продажами sales (как в задании 6). Выручка строки - quantity * price,
день продажи - дата invoice_date без времени.
"""

import pandas as pd


def daily_revenue(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте выручку за каждый календарный день от первого до последнего дня в sales.
    Верните Series: индекс - даты (datetime64, без времени) по порядку, значения - выручка;
    в дни без продаж - 0.
    """
    # TODO: ваш код здесь
    ...


def weekly_revenue(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте выручку по неделям. Неделя - с понедельника по воскресенье. Верните Series:
    индекс - дата понедельника каждой недели по порядку, от первой до последней недели в sales;
    значения - выручка за неделю, в неделях без продаж - 0. Первая и последняя недели могут
    быть неполными - считайте их как есть.
    """
    # TODO: ваш код здесь
    ...


def rolling_7d(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте для каждого календарного дня (как в daily_revenue) выручку за последние 7 дней,
    включая сам день. Для первых 6 дней, где 7 дней ещё не набралось, верните NaN.
    Верните Series с тем же индексом, что у daily_revenue.
    """
    # TODO: ваш код здесь
    ...


def week_over_week(sales: pd.DataFrame) -> pd.Series:
    """
    Посчитайте изменение недельной выручки (как в weekly_revenue) к предыдущей неделе в процентах:
    100 * (эта неделя - прошлая) / прошлая. Для первой недели и для недели после недели с нулевой
    выручкой верните NaN. Верните Series с тем же индексом, что у weekly_revenue.
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
    print(daily_revenue(sales).head(10))
    print(weekly_revenue(sales).tail(12))
    print(rolling_7d(sales).tail(10))
    print(week_over_week(sales).tail(12))
