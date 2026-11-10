"""
Задание 7. Выполним ли план.

Руководитель спрашивает, с какой вероятностью магазин выполнит месячный план.
Вы отвечаете симуляцией: много раз разыгрываете случайный месяц и смотрите,
как часто выручка дотягивает до плана.

Модель месяца: каждый из n_days дней магазин посещают visitors человек, каждый
покупает с вероятностью conversion. Сумма каждой покупки случайна:
экспоненциальное распределение со средним mean_check.
"""

import numpy as np


def simulate_month_revenue(
    n_sims: int, n_days: int, visitors: int, conversion: float, mean_check: float, seed: int
) -> np.ndarray:
    """
    Смоделируйте n_sims независимых месяцев и посчитайте выручку каждого.
    Верните массив формы (n_sims,). Случайные числа берите из генератора с seed:
    при одинаковом seed результат должен быть одинаковым.
    """
    # TODO: ваш код здесь
    ...


def prob_reach_target(revenues: np.ndarray, target: float) -> float:
    """
    Посчитайте долю симуляций, в которых выручка не меньше target.
    """
    # TODO: ваш код здесь
    ...


def min_conversion(
    target: float,
    prob: float,
    grid: np.ndarray,
    n_sims: int,
    n_days: int,
    visitors: int,
    mean_check: float,
    seed: int,
) -> float:
    """
    Маркетинг может поднять конверсию и спрашивает, до какого уровня. Найдите
    минимальную конверсию из grid, при которой вероятность выполнить план target
    не меньше prob. grid - возрастающий массив конверсий. Для каждой конверсии
    моделируйте выручку функцией simulate_month_revenue с переданными n_sims,
    n_days, visitors, mean_check и seed. Если ни одна конверсия из grid не подходит,
    верните np.nan.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    revenues = simulate_month_revenue(n_sims=10_000, n_days=30, visitors=200, conversion=0.05, mean_check=1500, seed=42)
    print("Средняя выручка:", revenues.mean())
    print("Вероятность выполнить план 450 000:", prob_reach_target(revenues, 450_000))
    grid = np.round(np.linspace(0.04, 0.08, 9), 3)
    print(
        "Нужная конверсия для плана 450 000 с вероятностью 90%:",
        min_conversion(450_000, 0.9, grid, n_sims=2_000, n_days=30, visitors=200, mean_check=1500, seed=42),
    )
