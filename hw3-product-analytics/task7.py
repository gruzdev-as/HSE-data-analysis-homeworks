"""
Задание 7. Отчёт по каналам привлечения: CAC и ROMI.

Работаете с очищенными events и users. Затраты на рекламу - spend (data/marketing_spend.csv):
week - понедельник недели, channel - канал, spend - затраты в рублях за неделю.
Выручка - покупки (purchase) минус возвраты (refund).
"""

import pandas as pd


def channel_report(users: pd.DataFrame, events: pd.DataFrame, spend: pd.DataFrame) -> pd.DataFrame:
    """
    Соберите отчёт по каналам за весь период данных. Канал пользователя - channel в users.
    Верните DataFrame: индекс - все каналы, которые есть в users или в spend, по алфавиту; столбцы:
        "users" - число пользователей канала (целое);
        "paying_users" - число пользователей канала с хотя бы одной покупкой (целое);
        "spend" - затраты на канал, 0 если затрат не было;
        "revenue" - выручка от пользователей канала;
        "cac" - затраты на одного пользователя канала;
        "romi" - (revenue - spend) / spend.
    Если затрат нет, cac и romi - NaN; если нет пользователей, cac - NaN.

    Пример: a и b пришли из ads_search, a купил на 3000; затраты на ads_search - 600 и 400
    за две недели -> users 2, paying_users 1, spend 1000, revenue 3000, cac 500, romi 2.0.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    events = pd.read_csv(DATA / "clean_events.csv", dtype={"user_id": "str"}, parse_dates=["event_ts", "event_date"])
    users = pd.read_csv(DATA / "clean_users.csv", dtype={"user_id": "str"}, parse_dates=["signup_date"])
    spend = pd.read_csv(DATA / "marketing_spend.csv", parse_dates=["week"])
    print(channel_report(users, events, spend).round(2))
