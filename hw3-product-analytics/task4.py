"""
Задание 4. Отчёт по аудитории: DAU, WAU, MAU.

Работаете с очищенным логом events (data/clean_events.csv). Активный пользователь за день - тот,
у кого в этот день (event_date) есть хотя бы одно событие любого типа.
"""

import pandas as pd


def audience_report(events: pd.DataFrame) -> dict:
    """
    Соберите отчёт по аудитории за каждый календарный день от первого до последнего дня в events.
    Верните словарь из четырёх Series с одинаковым индексом - даты по порядку:
        "dau" - число активных пользователей за день (целые числа);
        "wau" - число пользователей, активных хотя бы в один из 7 последних дней, включая сам день;
            для первых 6 дней - NaN;
        "mau" - то же за 28 последних дней; для первых 27 дней - NaN;
        "stickiness" - dau / mau; где mau не определён, - NaN.

    Пример: a активен 01.01 и 07.01, b - 03.01, данные с 01.01 по 07.01 -> dau 1, 0, 1, 0, 0, 0, 1;
    wau NaN за 01.01-06.01 и 2 за 07.01.
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
    print(pd.DataFrame(audience_report(events)).tail(10))
