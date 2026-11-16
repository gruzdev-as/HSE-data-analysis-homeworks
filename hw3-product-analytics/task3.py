"""
Задание 3. Монетизация: ARPU, ARPPU, средний чек.

Здесь и дальше работаете с очищенным логом events (data/clean_events.csv): user_id, event,
event_ts, event_date, amount. Выручка - сумма amount покупок (purchase) минус сумма amount
возвратов (refund). Период - с start по end включительно (даты "ГГГГ-ММ-ДД"), день события -
event_date.
"""

import pandas as pd


def arpu(events: pd.DataFrame, start: str, end: str) -> float:
    """
    Посчитайте ARPU за период - выручку на активного пользователя (хотя бы одно событие любого
    типа за период). Если активных нет, верните NaN.

    Пример: a купил на 1000 и вернул 200, b только открыл приложение -> (1000 - 200) / 2 = 400.
    """
    # TODO: ваш код здесь
    ...


def arppu(events: pd.DataFrame, start: str, end: str) -> float:
    """
    Посчитайте ARPPU за период - выручку на платящего пользователя (хотя бы одна покупка за период).
    Если платящих нет, верните NaN.

    Пример: a купил на 1000 и вернул 200, b только открыл приложение -> (1000 - 200) / 1 = 800.
    """
    # TODO: ваш код здесь
    ...


def average_check(events: pd.DataFrame, start: str, end: str) -> float:
    """
    Посчитайте средний чек за период - среднюю сумму одной покупки. Если покупок нет, верните NaN.

    Пример: у a покупки на 1000 и 500, у b - на 300 -> (1000 + 500 + 300) / 3 = 600.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    events = pd.read_csv(
        Path(__file__).parent / "data" / "clean_events.csv",
        dtype={"user_id": "str"},
        parse_dates=["event_ts", "event_date"],
    )
    for start, end in [("2025-12-01", "2025-12-31"), ("2026-01-01", "2026-01-31")]:
        print(start, end, arpu(events, start, end), arppu(events, start, end), average_check(events, start, end))
