"""
Задание 5. Ближайший пункт выдачи.

Магазин решает, какие пункты выдачи оставить. Вы пишете функции, которые
закрепляют клиентов за ближайшими пунктами. Работаете с координатами на карте:
- customers - клиенты, форма (n, 2): строка - координаты (x, y) одного клиента;
- points - пункты выдачи, форма (m, 2): строка - координаты одного пункта.
"""

import numpy as np


def distance_matrix(customers: np.ndarray, points: np.ndarray) -> np.ndarray:
    """
    Посчитайте евклидово расстояние от каждого клиента до каждого пункта.
    Верните матрицу формы (n, m): элемент [i, j] - расстояние от клиента i до пункта j.

    Пример:
        distance_matrix(np.array([[0, 0]]), np.array([[3, 4], [0, 1]])) -> [[5.0, 1.0]]
    """
    # TODO: ваш код здесь
    ...


def nearest_point(customers: np.ndarray, points: np.ndarray) -> np.ndarray:
    """
    Для каждого клиента найдите ближайший пункт. Верните индексы пунктов,
    форма (n,). При равенстве расстояний верните меньший индекс.
    """
    # TODO: ваш код здесь
    ...


def point_load(customers: np.ndarray, points: np.ndarray) -> np.ndarray:
    """
    Посчитайте, для скольких клиентов каждый пункт - ближайший.
    Верните массив формы (m,).

    Пример:
        point_load(np.array([[0, 0], [1, 0]]), np.array([[0, 0], [9, 9]])) -> [2, 0]
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    rng = np.random.default_rng(0)
    customers = rng.uniform(0, 10, size=(8, 2))
    points = np.array([[2.0, 2.0], [8.0, 3.0], [5.0, 8.0], [20.0, 20.0]])
    print("Расстояния:\n", distance_matrix(customers, points).round(2))
    print("Ближайшие пункты:", nearest_point(customers, points))
    print("Загрузка пунктов:", point_load(customers, points))
