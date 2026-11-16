"""
Задание 5. Воронка.

Работаете с очищенным логом events (data/clean_events.csv).
"""

import pandas as pd


def funnel(events: pd.DataFrame, steps: list[str]) -> pd.DataFrame:
    """
    Постройте воронку по шагам steps - списку типов событий, например
    ["view_item", "add_to_cart", "checkout", "purchase"].

    Пользователь проходит первый шаг, если у него есть такое событие; время прохождения - первое
    такое событие. Следующий шаг он проходит, если прошёл предыдущий и у него есть событие этого
    шага не раньше, чем он прошёл предыдущий; время прохождения - первое такое событие.

    Верните DataFrame с индексом steps (в том же порядке) и столбцами:
        "users" - сколько пользователей прошли шаг (целое число);
        "conv_prev" - users / users предыдущего шага, у первого шага - 1.0;
        "conv_first" - users / users первого шага.
    Где делить на 0, - NaN.

    Пример: steps ["view_item", "purchase"]; a посмотрел товар и купил, b только посмотрел ->
    users 2, 1; conv_prev 1.0, 0.5; conv_first 1.0, 0.5.
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
    print(funnel(events, ["app_open", "view_item", "add_to_cart", "checkout", "purchase"]))
