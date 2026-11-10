"""
Задание 9. Почините код ассистента.

ИИ-ассистент написал функции для отчёта по продажам. Описания функций
(докстринги) верные, а в коде есть ошибки. Найдите и исправьте их, не меняя
сигнатуры и описания. В функции может быть больше одной ошибки.
"""

import numpy as np


def mean_per_product(sales: np.ndarray) -> np.ndarray:
    """
    Возвращает средние продажи каждого товара в день.
    sales - форма (n_products, n_days), результат - форма (n_products,).
    """
    return sales.mean(axis=0)


def peak_cell(revenue: np.ndarray) -> tuple[int, int]:
    """
    Возвращает пару (товар, день) с максимальной выручкой.
    revenue - форма (n_products, n_days). При равенстве - первая пара при обходе по строкам.
    """
    idx = np.argmax(revenue)
    return int(idx // revenue.shape[0]), int(idx % revenue.shape[0])


def row_shares(matrix: np.ndarray) -> np.ndarray:
    """
    Возвращает долю каждого элемента в сумме своей строки, форма как у matrix.
    Для строки из нулей - нули.
    """
    return matrix / matrix.sum(axis=1)


def count_in_range(values: np.ndarray, low: float, high: float) -> int:
    """
    Возвращает, сколько значений лежит в отрезке [low, high], включая обе границы.
    """
    return int(np.logical_and(values >= low, values < high).sum())


def fill_missing(amounts: np.ndarray, value: float) -> np.ndarray:
    """
    Возвращает копию amounts, в которой np.nan заменены на value.
    Исходный массив не меняется.
    """
    result = amounts
    result[result == np.nan] = value
    return result


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    sales = np.loadtxt(DATA / "sales.csv", delimiter=",", dtype=int)
    prices = np.loadtxt(DATA / "prices.csv")
    print("Среднее по товарам, первые 5:", mean_per_product(sales)[:5])
    print("Пик выручки (товар, день):", peak_cell(sales * prices[:, np.newaxis]))
    print("Доли дней по товару 0, первые 5:", row_shares(sales)[0, :5])
    print("Цен в отрезке [199, 990]:", count_in_range(prices, 199, 990))
    amounts = np.loadtxt(DATA / "amounts.csv")
    print("Чеки без пропусков, первые 10:", fill_missing(amounts, 0.0)[:10])
