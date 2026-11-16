"""
Задание 1. Загрузка лога событий.

Приложение отправляет события на сервер, сервер пишет их в выгрузку data/events.csv:
- event_id - номер события, его присваивает приложение;
- user_id - пользователь;
- event - тип события: app_open, view_item, add_to_cart, checkout, purchase, refund;
- event_ts - когда событие произошло, received_at - когда сервер его получил (оба в UTC);
- amount - сумма в рублях у purchase (покупка) и refund (возврат), у остальных пусто.

Пользователи - data/users.csv: user_id, signup_ts (время регистрации в UTC), channel - откуда
пришёл пользователь, platform - ios, android или web.

Аналитика компании ведётся по московскому времени.
"""

from pathlib import Path

import pandas as pd


def load_events(path: str | Path) -> pd.DataFrame:
    """
    Загрузите выгрузку событий. Верните DataFrame со столбцами event_id, user_id, event,
    event_ts, received_at, amount, event_date:
    - user_id и event - строки, event_id - целое число, amount - float;
    - event_ts и received_at - московское время, datetime64 без часового пояса;
    - event_date - дата события по Москве (datetime64, время 00:00).
    Порядок строк - как в файле.

    Пример: строка "101,512345,app_open,2026-01-10T09:30:00Z,2026-01-10T09:30:02Z," превращается в
    event_id 101, user_id "512345", event_ts 2026-01-10 12:30:00, event_date 2026-01-10, amount NaN.
    """
    # TODO: ваш код здесь
    ...


def load_users(path: str | Path) -> pd.DataFrame:
    """
    Загрузите таблицу пользователей. Верните DataFrame со столбцами user_id, signup_ts, channel,
    platform, signup_date: user_id, channel, platform - строки, signup_ts - московское время
    (datetime64 без часового пояса), signup_date - дата регистрации по Москве (время 00:00).

    Пример: строка "512345,2026-01-10T09:30:00Z,organic,ios" превращается в user_id "512345",
    signup_ts 2026-01-10 12:30:00, channel "organic", platform "ios", signup_date 2026-01-10.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    DATA = Path(__file__).parent / "data"
    events = load_events(DATA / "events.csv")
    users = load_users(DATA / "users.csv")
    print(events.dtypes, events.head(), sep="\n\n")
    print(users.head())
