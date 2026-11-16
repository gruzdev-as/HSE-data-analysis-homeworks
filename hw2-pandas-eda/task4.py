"""
Задание 4. Чистка выгрузки.

Работаете с выгрузкой заказов orders (столбцы - как в задании 1, invoice_date и loaded_at -
datetime64, customer_id - Int64), справочником клиентов customers (data/customers.csv:
customer_id, email, segment, signup_date, updated_at) и курсами валют fx_rates
(data/fx_rates.csv):
- date - дата (datetime64, без времени), курсы есть на каждый календарный день периода;
- currency - валюта (EUR, USD);
- units_per_gbp - сколько единиц валюты стоит 1 фунт в этот день.
С июля часть счетов выставляется не в фунтах: price указан в валюте счёта (столбец currency).
Функции не должны менять переданные данные.
"""

import pandas as pd

TEST_DOMAIN = "test.retail.co.uk"


def drop_export_duplicates(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Иногда учётная система выгружает одну и ту же строку счёта повторно (следующей ночью).
    Дубль выгрузки - строка с теми же invoice и line_no, что у одной из строк выше.
    Удалите дубли, оставив для каждой пары (invoice, line_no) первую по порядку строку.
    Порядок оставшихся строк не меняйте.

    Пример: строки (invoice, line_no) = (10, 1), (10, 2), (10, 1) -> остаются первые две.
    """
    # TODO: ваш код здесь
    ...


def to_gbp(orders: pd.DataFrame, fx_rates: pd.DataFrame) -> pd.DataFrame:
    """
    Переведите цены в фунты по курсу дня счёта. Верните копию orders, в которой price - цена
    за штуку в фунтах, а currency - "GBP". Число и порядок строк - как в orders, индекс тот же.

    Пример: price 12.0 в EUR в день, когда units_per_gbp = 1.2, -> price 10.0, currency "GBP".
    """
    # TODO: ваш код здесь
    ...


def clean_orders(orders: pd.DataFrame, customers: pd.DataFrame, fx_rates: pd.DataFrame) -> dict:
    """
    Очистите выгрузку по шагам:
    1. удалите дубли выгрузки (как в drop_export_duplicates);
    2. удалите строки тестовых аккаунтов - клиентов, у которых email на домене
       test.retail.co.uk (TEST_DOMAIN);
    3. отделите отмены - строки, номер счёта которых начинается с буквы C;
    4. из остальных строк удалите некорректные: quantity <= 0 или price <= 0;
    5. переведите цены продаж и отмен в фунты (как в to_gbp).
    Верните словарь:
        "sales" - продажи после всех шагов; "cancellations" - отмены после шагов 1, 2 и 5
            (у обеих частей порядок строк и индекс - как в orders);
        "stats" - словарь, сколько строк удалено или отделено на каждом шаге:
            {"export_duplicates": ..., "test_rows": ..., "cancellations": ..., "invalid_rows": ...}.

    Пример: из 100 строк 3 - дубли выгрузки, 5 - тестового аккаунта, 4 - отмены, 2 - с нулевой
    ценой -> в "sales" 86 строк, stats = {"export_duplicates": 3, "test_rows": 5,
    "cancellations": 4, "invalid_rows": 2}.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    orders = pd.read_csv(
        DATA / "orders_iso.csv",
        dtype={"invoice": "str", "stock_code": "str", "customer_id": "Int64"},
        parse_dates=["invoice_date", "loaded_at"],
    )
    customers = pd.read_csv(DATA / "customers.csv", parse_dates=["signup_date", "updated_at"])
    fx_rates = pd.read_csv(DATA / "fx_rates.csv", parse_dates=["date"])
    print("Строк до и после удаления дублей:", len(orders), len(drop_export_duplicates(orders)))
    converted = to_gbp(orders, fx_rates)
    print(converted[orders["currency"] != "GBP"][["invoice", "price", "currency"]].head())
    result = clean_orders(orders, customers, fx_rates)
    print("Продаж:", len(result["sales"]), "отмен:", len(result["cancellations"]))
    print(result["stats"])
