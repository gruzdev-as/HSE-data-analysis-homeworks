"""
Задание 10*. Симуляция воронки.

Маркетинг хочет понять, насколько может «гулять» конверсия рекламной кампании.
Вы отвечаете симуляцией. Модель кампании: рекламу показали n_impressions раз,
каждый показ даёт клик с вероятностью p_click, каждый клик даёт покупку
с вероятностью p_buy.
"""

import numpy as np


def simulate_funnel(n_impressions: int, p_click: float, p_buy: float, n_sims: int, seed: int) -> np.ndarray:
    """
    Смоделируйте n_sims независимых рекламных кампаний. Верните массив формы
    (n_sims, 3): столбцы - показы, клики, покупки. Случайные числа берите
    из генератора с seed: при одинаковом seed результат должен быть одинаковым.
    """
    # TODO: ваш код здесь
    ...


def conversion_interval(funnel: np.ndarray, level: float) -> tuple[float, float]:
    """
    funnel - результат simulate_funnel. Посчитайте конверсию из показа в покупку
    в каждой симуляции и верните интервал (low, high), в который попадает доля level
    симуляций: квантили (1 - level) / 2 и (1 + level) / 2.
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    funnel = simulate_funnel(n_impressions=10_000, p_click=0.03, p_buy=0.1, n_sims=5_000, seed=1)
    print("Первые 3 симуляции:\n", funnel[:3])
    print("90%-интервал конверсии:", conversion_interval(funnel, 0.9))
