"""
Задание 2. Чистка лога и DAU.

events - лог событий со столбцами как после load_events из задания 1: event_id, user_id, event,
event_ts, received_at, amount, event_date (время московское). users - пользователи: user_id,
channel и другие столбцы. Функции не должны менять переданные DataFrame.
"""

import pandas as pd


def drop_resent_events(events: pd.DataFrame) -> pd.DataFrame:
    """
    Приложение иногда отправляет одно и то же событие повторно. Оставьте у каждого event_id одну
    строку - ту, что сервер получил раньше (received_at меньше). Верните новый DataFrame:
    оставшиеся строки в исходном порядке, индекс как в events.

    Пример: строки с event_id 7, 8, 7 и received_at 12:00:09, 12:00:03, 12:00:01 -> остаются
    вторая и третья строки (event_id 8 и 7).
    """
    # TODO: ваш код здесь
    ...


def remove_internal(events: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """
    Удалите события служебных аккаунтов сотрудников - пользователей с channel == "internal" в users.
    Верните новый DataFrame: оставшиеся строки в исходном порядке, индекс как в events.

    Пример: у пользователя "000042" channel "internal" -> все его события удаляются, события
    остальных пользователей остаются.
    """
    # TODO: ваш код здесь
    ...


def dau(events: pd.DataFrame) -> pd.Series:
    """
    Посчитайте DAU - число активных пользователей (хотя бы одно событие любого типа) за каждый
    календарный день от первого до последнего дня в events. День - event_date. Верните Series:
    индекс - даты по порядку, значения - целые числа.

    Пример: 10.01 события у a (три) и b, 12.01 - у a -> DAU 2, 0, 1 за 10.01, 11.01, 12.01.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    raw = pd.read_csv(DATA / "events.csv", dtype={"user_id": "str"}, parse_dates=["event_ts", "received_at"])
    users = pd.read_csv(DATA / "users.csv", dtype={"user_id": "str"})
    once = drop_resent_events(raw)
    clean = remove_internal(once, users)
    print(f"Строк было {len(raw)}, без повторов {len(once)}, без сотрудников {len(clean)}")
    events = pd.read_csv(DATA / "clean_events.csv", dtype={"user_id": "str"}, parse_dates=["event_ts", "event_date"])
    print(dau(events).tail(10))
