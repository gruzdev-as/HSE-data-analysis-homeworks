"""
Задание 6. Сегменты клиентов.

Работаете с чистыми продажами sales (столбцы - как в задании 3) и справочником клиентов
customers (data/customers.csv): customer_id, email, segment, signup_date, updated_at (datetime64).
Когда профиль клиента меняется, в справочник дописывается новая строка с тем же customer_id,
актуальна строка с самым поздним updated_at. Порядок строк в справочнике произвольный.
"""

import pandas as pd


def latest_profiles(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Оставьте для каждого клиента одну, актуальную строку. Верните DataFrame с теми же
    столбцами, по возрастанию customer_id, индекс 0, 1, 2, ...

    Пример: у клиента 5 строки с segment "retail" (updated_at 2010-01-10) и "vip"
    (updated_at 2010-06-01) -> остаётся строка "vip".
    """
    # TODO: ваш код здесь
    ...


def segment_report(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """
    Соберите отчёт по актуальным сегментам клиентов (как в latest_profiles). Продажи без
    customer_id отнесите к сегменту "guest", продажи клиентов, которых нет в справочнике, -
    к "unknown". Верните DataFrame: индекс - сегмент, строки по убыванию выручки, при
    равенстве - по алфавиту; столбцы:
        "revenue" - выручка (quantity * price);
        "share" - доля выручки сегмента в общей выручке (от 0 до 1);
        "invoices" - число счетов;
        "buyers" - число разных клиентов (у "guest" - 0);
        "aov" - средний чек, средняя сумма одного счёта.

    Пример: клиент 1 (vip) - один счёт на 300, гость - счёт на 100 -> vip: revenue 300,
    share 0.75, invoices 1, buyers 1, aov 300; guest: 100, 0.25, 1, 0, 100.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    sales = pd.read_csv(
        DATA / "sales.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date"],
    )
    customers = pd.read_csv(DATA / "customers.csv", parse_dates=["signup_date", "updated_at"])
    print(latest_profiles(customers).head())
    print(segment_report(sales, customers))
