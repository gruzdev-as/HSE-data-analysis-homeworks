"""
Задание 6. Похожие покупатели и корзины.

Вы пишете функции для рекомендаций и расчёта корзин. Работаете с матрицей
ratings - «пользователь × товар», форма (n_users, n_products): ratings[u, i] -
сколько раз пользователь u купил товар i. У каждого пользователя своя строка -
вектор его покупок.
"""

import numpy as np


def cosine_similarity_matrix(ratings: np.ndarray) -> np.ndarray:
    """
    Посчитайте косинусную близость покупок для каждой пары пользователей.
    Верните матрицу формы (n_users, n_users). Если у пользователя нет покупок,
    его близость со всеми (и с собой) считайте равной 0.
    """
    # TODO: ваш код здесь
    ...


def most_similar_user(ratings: np.ndarray, user: int) -> int:
    """
    Найдите пользователя, чьи покупки больше всего похожи (по косинусной близости)
    на покупки пользователя user. Сам user не считается. Верните индекс найденного
    пользователя. При равенстве верните меньший индекс.
    """
    # TODO: ваш код здесь
    ...


def basket_totals(baskets: np.ndarray, prices: np.ndarray, discounts: np.ndarray) -> np.ndarray:
    """
    Посчитайте стоимость каждой корзины с учётом скидок.
    baskets - корзины в штуках, форма (n_baskets, n_products).
    prices - цены, discounts - скидки в долях от 0 до 1, обе формы (n_products,).
    Верните массив формы (n_baskets,).

    Пример:
        basket_totals(np.array([[1, 2]]), np.array([100, 10]), np.array([0.5, 0])) -> [70.0]
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    ratings = np.loadtxt(DATA / "ratings.csv", delimiter=",", dtype=int)
    print("Близость, первые 3 x 3:\n", cosine_similarity_matrix(ratings)[:3, :3].round(3))
    print("Самый похожий на пользователя 0:", most_similar_user(ratings, 0))
    baskets = np.loadtxt(DATA / "baskets.csv", delimiter=",", dtype=int)
    prices, discounts = np.loadtxt(DATA / "catalog.csv", delimiter=",", skiprows=1, unpack=True)
    print("Стоимость первых 5 корзин:", basket_totals(baskets, prices, discounts)[:5])
