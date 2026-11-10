"""
Задание 9. Почините код ассистента.

ИИ-ассистент написал функции для отчёта по чистым продажам sales (столбцы как в задании 6).
Описания функций (докстринги) верные, а в коде есть ошибки. Найдите и исправьте их, не меняя
сигнатуры и описания. В функции может быть больше одной ошибки.
"""

import pandas as pd


def fill_unknown_country(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает копию sales, в которой пропуски в country заменены на "Unspecified".
    Исходный DataFrame не меняется.
    """
    result = sales
    result["country"].fillna("Unspecified", inplace=True)
    return result


def count_buyers(sales: pd.DataFrame) -> int:
    """
    Возвращает число разных клиентов. Гостевые продажи (без customer_id) не учитываются.
    """
    return int(sales["customer_id"].count())


def big_orders(sales: pd.DataFrame, min_total: float) -> list[str]:
    """
    Возвращает номера счетов, сумма которых (сумма quantity * price по всем строкам счёта)
    не меньше min_total. Список строк по возрастанию.
    """
    big = sales[sales["quantity"] * sales["price"] > min_total]
    return list(big["invoice"].unique())


def monthly_revenue(sales: pd.DataFrame) -> pd.Series:
    """
    Возвращает выручку по месяцам: индекс - месяц строкой "ГГГГ-ММ" по порядку, значения - выручка.
    """
    sales = sales.assign(revenue=sales["quantity"] * sales["price"])
    revenue = sales.groupby(sales["invoice_date"].dt.month)["revenue"].sum()
    revenue.index = [f"{sales['invoice_date'].dt.year.min()}-{m:02d}" for m in revenue.index]
    return revenue


def add_email(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает sales с добавленным столбцом email из справочника customers (у одного клиента
    может быть несколько строк в справочнике, email в них одинаковый). Число и порядок строк -
    как в sales; у гостевых продаж и клиентов не из справочника email пустой.
    """
    return sales.merge(customers[["customer_id", "email"]], on="customer_id")


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
    print("Пропусков в country после замены:", fill_unknown_country(sales)["country"].isna().sum())
    print("Клиентов:", count_buyers(sales))
    print("Счетов от 1000 фунтов:", len(big_orders(sales, 1000)))
    print(monthly_revenue(sales))
    print("Строк до и после добавления email:", len(sales), len(add_email(sales, customers)))
