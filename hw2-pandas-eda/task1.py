"""
Задание 1. Загрузка выгрузки заказов.

Учётная система магазина каждую ночь выгружает строки заказов в CSV (пример - data/orders.csv).
Одна строка - одна позиция счёта. Столбцы:
- invoice - номер счёта; счета-отмены начинаются с буквы C;
- line_no - номер строки внутри счёта;
- stock_code, description - код и описание товара;
- quantity - количество, price - цена за штуку в валюте счёта, currency - валюта счёта;
- invoice_date - дата и время счёта в формате ДД.ММ.ГГГГ ЧЧ:ММ;
- customer_id - номер клиента, пусто у гостевых заказов;
- country - страна клиента;
- loaded_at - дата и время выгрузки строки, формат как у invoice_date.
"""

from pathlib import Path

import pandas as pd


def load_orders(path: str | Path) -> pd.DataFrame:
    """
    Прочитайте CSV-выгрузку заказов. Верните DataFrame с теми же столбцами и типами:
    - invoice, stock_code, description, currency, country - строки (str);
    - line_no, quantity - целые (int64);
    - price - дробное (float64);
    - invoice_date, loaded_at - дата и время (datetime64);
    - customer_id - целое с пропусками (Int64).
    """
    # TODO: ваш код здесь
    ...


def summary(orders: pd.DataFrame) -> dict:
    """
    Посчитайте краткую сводку по загруженной выгрузке orders. Верните словарь с ключами:
    - "n_rows" - число строк;
    - "n_invoices" - число разных счетов;
    - "n_customers" - число разных клиентов (гостевые заказы - не клиенты);
    - "guest_share" - доля счетов без клиента среди всех счетов (от 0 до 1);
    - "first_date", "last_date" - даты (без времени) первого и последнего счёта, pd.Timestamp.
    Для пустой выгрузки: числа - 0, guest_share - 0.0, даты - None.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    DATA = Path(__file__).parent / "data"
    orders = load_orders(DATA / "orders.csv")
    print(orders.dtypes)
    print(orders.head())
    print(summary(orders))
