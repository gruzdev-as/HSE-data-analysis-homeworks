"""
Задание 1. Загрузка и выборки.

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
Функции не должны менять переданный DataFrame.
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

    Пример: строка "536365,1,85123A,...,25.03.2010 08:26,...,17850.0,..." превращается в
    invoice "536365", invoice_date 2010-03-25 08:26, customer_id 17850.
    """
    # TODO: ваш код здесь
    ...


def add_line_total(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Верните копию orders с новым столбцом line_total - сумма строки (quantity * price).

    Пример: строка с quantity 6 и price 2.55 получает line_total 15.3.
    """
    # TODO: ваш код здесь
    ...


def orders_in_period(orders: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """
    Верните строки, у которых дата счёта лежит в периоде с start по end включительно.
    start и end - даты в формате "ГГГГ-ММ-ДД". Порядок строк - как в orders.

    Пример: orders_in_period(orders, "2010-12-01", "2010-12-31") - все строки декабря 2010.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    DATA = Path(__file__).parent / "data"
    orders = load_orders(DATA / "orders.csv")
    print(orders.dtypes)
    print(add_line_total(orders).head())
    print("Строк за декабрь 2010:", len(orders_in_period(orders, "2010-12-01", "2010-12-31")))
