"""
Задание 7. Сегменты клиентов.

Работаете с чистыми продажами sales (как в задании 6) и справочником клиентов customers
(data/customers.csv): customer_id, email, segment, signup_date, updated_at (datetime64).
Когда профиль клиента меняется, в справочник дописывается новая строка с тем же customer_id,
актуальна строка с самым поздним updated_at. Порядок строк в справочнике произвольный.
"""

import pandas as pd


def latest_profiles(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Оставьте для каждого клиента одну, актуальную строку. Верните DataFrame с теми же
    столбцами, по возрастанию customer_id, индекс 0, 1, 2, ...
    """
    # TODO: ваш код здесь
    ...


def revenue_by_segment(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.Series:
    """
    Посчитайте выручку по актуальным сегментам клиентов. Продажи без customer_id отнесите к
    сегменту "guest", продажи клиентов, которых нет в справочнике, - к "unknown".
    Верните Series: индекс - сегмент, значения - выручка, по убыванию.
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
    print(revenue_by_segment(sales, customers))
