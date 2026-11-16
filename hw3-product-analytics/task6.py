"""
Задание 6. Когорты: удержание и накопительный LTV.

Работаете с очищенными events (data/clean_events.csv) и users (data/clean_users.csv:
user_id, signup_date, channel, platform; signup_date - дата регистрации, время 00:00).

Когорта пользователя - неделя его регистрации: дата понедельника этой недели (неделя - с
понедельника по воскресенье). Неделя жизни k пользователя - дни с 7k по 7k + 6 после дня
регистрации (день регистрации - день 0, то есть неделя 0 - дни 0-6). Выручка - покупки (purchase)
минус возвраты (refund).
"""

import pandas as pd


def cohort_report(events: pd.DataFrame, users: pd.DataFrame, end_date: str) -> dict:
    """
    Соберите когортный отчёт по данным до end_date включительно ("ГГГГ-ММ-ДД"). Верните словарь:
        "sizes" - Series: индекс - понедельники от первой до последней когорты по порядку,
            значения - число пользователей когорты (целые, в неделях без регистраций - 0);
        "retention" - DataFrame: строки - когорты (как в sizes), столбцы - k = 0, 1, 2, ...;
            клетка - доля пользователей когорты, у которых есть хотя бы одно событие в неделю жизни k;
        "ltv" - DataFrame той же формы: клетка - выручка от пользователей когорты за недели жизни
            0..k, делённая на размер когорты.
    Столбцы - до последней недели, которая к end_date закончилась у всех пользователей хотя бы
    одной когорты. Если неделя k ещё не закончилась к end_date хотя бы у одного пользователя
    когорты, клетка - NaN (в обеих таблицах).

    Пример: a зарегистрировался 05.01.2026 (понедельник), b - 07.01, c - 12.01; события: a - 05.01
    и покупка на 1000 14.01, b - 07.01, c - 12.01; end_date "2026-01-25" -> sizes: 05.01 - 2,
    12.01 - 1; retention: 05.01 - 1.0, 0.5; 12.01 - 1.0, 0.0; ltv: 05.01 - 0, 500; 12.01 - 0, 0.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    events = pd.read_csv(DATA / "clean_events.csv", dtype={"user_id": "str"}, parse_dates=["event_ts", "event_date"])
    users = pd.read_csv(DATA / "clean_users.csv", dtype={"user_id": "str"}, parse_dates=["signup_date"])
    report = cohort_report(events, users, "2026-02-28")
    print(report["sizes"])
    print(report["retention"].round(2).iloc[:, :8])
    print(report["ltv"].round(0).iloc[:, :8])
