"""
Задание 2. Матрица продаж.

Вы пишете функции для отчёта по товарам. Работаете с двумя массивами:
- sales - продажи в штуках, форма (n_products, n_days): строка - товар, столбец - день;
- prices - цены товаров, форма (n_products,): prices[i] - цена товара из строки i.
"""

import numpy as np


def revenue_matrix(sales: np.ndarray, prices: np.ndarray) -> np.ndarray:
    """
    Посчитайте выручку каждого товара в каждый день (штуки × цена).
    Верните матрицу той же формы, что sales.
    """
    # TODO: ваш код здесь
    ...


def daily_revenue(sales: np.ndarray, prices: np.ndarray) -> np.ndarray:
    """
    Посчитайте выручку всего магазина за каждый день.
    Верните массив формы (n_days,).
    """
    # TODO: ваш код здесь
    ...


def best_product(sales: np.ndarray, prices: np.ndarray) -> int:
    """
    Найдите товар, который принёс больше всего выручки за весь период.
    Верните его индекс. При равенстве верните меньший индекс.
    """
    # TODO: ваш код здесь
    ...


def zero_sales_days(sales: np.ndarray) -> int:
    """
    Посчитайте, сколько было дней, в которые не продали ни одного товара.
    """
    # TODO: ваш код здесь
    ...


def order_totals(orders: np.ndarray, prices: np.ndarray, discounts: np.ndarray) -> np.ndarray:
    """
    Посчитайте сумму каждого заказа с учётом скидок.
    orders - заказы в штуках, форма (n_orders, n_products): orders[k, i] - сколько
    штук товара i в заказе k. discounts - скидки на товары в долях от 0 до 1,
    форма (n_products,). Верните массив формы (n_orders,).

    Пример:
        order_totals(np.array([[1, 2]]), np.array([100, 10]), np.array([0.5, 0])) -> [70.0]
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    sales = np.loadtxt(DATA / "sales.csv", delimiter=",", dtype=int)
    prices = np.loadtxt(DATA / "prices.csv")
    print("Выручка, первые 3 товара x 5 дней:\n", revenue_matrix(sales, prices)[:3, :5])
    print("Выручка по дням, первые 7:", daily_revenue(sales, prices)[:7])
    print("Лучший товар:", best_product(sales, prices))
    print("Дней без продаж:", zero_sales_days(sales))
    orders = np.loadtxt(DATA / "orders.csv", delimiter=",", dtype=int)
    discounts = np.loadtxt(DATA / "discounts.csv")
    print("Суммы первых 5 заказов:", order_totals(orders, prices, discounts)[:5])
