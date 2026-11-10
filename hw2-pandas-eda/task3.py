"""
Задание 3. Чистка: дубли выгрузки, тестовые аккаунты, отмены.

Работаете с выгрузкой orders в виде, как её возвращает load_orders из задания 1, и
справочником клиентов customers (data/customers.csv): customer_id, email, segment,
signup_date, updated_at. Функции не должны менять переданные DataFrame.
"""

import pandas as pd

TEST_DOMAIN = "test.retail.co.uk"


def drop_export_duplicates(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Иногда учётная система выгружает одну и ту же строку счёта повторно (следующей ночью).
    Дубль выгрузки - строка с теми же invoice и line_no, что у одной из строк выше.
    Удалите дубли, оставив для каждой пары (invoice, line_no) первую по порядку строку.
    Порядок оставшихся строк не меняйте.
    """
    # TODO: ваш код здесь
    ...


def remove_test_accounts(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """
    Тестовые аккаунты - клиенты, у которых email на домене test.retail.co.uk (TEST_DOMAIN).
    Удалите из orders строки тестовых аккаунтов, остальные строки верните без изменений
    и в том же порядке.
    """
    # TODO: ваш код здесь
    ...


def split_cancellations(orders: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Разделите строки на обычные и отмены. Отмена - строка, номер счёта которой начинается
    с буквы C. Верните пару (обычные строки, отмены), порядок строк внутри каждой части -
    как в orders.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    from task1 import load_orders

    DATA = Path(__file__).parent / "data"
    orders = load_orders(DATA / "orders.csv")
    customers = pd.read_csv(DATA / "customers.csv")
    deduped = drop_export_duplicates(orders)
    print("Строк до и после удаления дублей:", len(orders), len(deduped))
    real = remove_test_accounts(deduped, customers)
    print("Строк без тестовых аккаунтов:", len(real))
    sales, cancellations = split_cancellations(real)
    print("Обычных строк:", len(sales), "отмен:", len(cancellations))
