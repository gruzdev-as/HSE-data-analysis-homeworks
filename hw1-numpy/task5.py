"""
Задание 5. Сегментация клиентов.

Маркетинг описал сегменты клиентов через «типичного представителя» каждого
сегмента. Вы пишете функции, которые относят каждого клиента к ближайшему
сегменту и описывают получившиеся сегменты. Работаете с матрицами:
- X - признаки клиентов, форма (n_clients, n_features), целые числа: строка - клиент,
  столбец - признак (возраст, число визитов, средний чек и т.д.);
- centers - типичные представители сегментов в тех же признаках и единицах,
  форма (n_segments, n_features).
Исходные массивы менять нельзя.
"""

import numpy as np


def scale_features(X: np.ndarray, method: str, reference: np.ndarray | None = None) -> np.ndarray:
    """
    Приведите признаки к одному масштабу, каждый столбец отдельно:
        method="minmax": (x - min) / (max - min);
        method="zscore": (x - mean) / std, std с ddof=0.
    min, max, mean и std берите по столбцам reference, а если reference не передан -
    по столбцам самого X. Если столбец reference постоянный, значения этого
    столбца в результате - нули. При другом method вызовите ValueError.
    Верните float-массив той же формы, что X.

    Пример:
        scale_features(np.array([[1, 5], [3, 5]]), "minmax") -> [[0.0, 0.0], [1.0, 0.0]]
        scale_features(np.array([[2, 5]]), "minmax", np.array([[1, 5], [3, 5]])) -> [[0.5, 0.0]]
    """
    # TODO: ваш код здесь
    ...


def assign_segments(X: np.ndarray, centers: np.ndarray, method: str) -> np.ndarray:
    """
    Отнесите каждого клиента к ближайшему сегменту. Сначала отмасштабируйте признаки
    клиентов и центров через scale_features с методом method; статистики для обоих
    массивов считайте по клиентам X. Затем для каждого клиента найдите центр
    с наименьшим евклидовым расстоянием в отмасштабированных признаках.
    Верните номера сегментов, форма (n_clients,). При равенстве - меньший номер.
    """
    # TODO: ваш код здесь
    ...


def segment_summary(X: np.ndarray, labels: np.ndarray, n_segments: int) -> dict:
    """
    labels - номера сегментов клиентов (результат assign_segments), сегменты
    нумеруются от 0 до n_segments - 1. Опишите сегменты. Верните словарь:
        "size" - число клиентов в каждом сегменте, форма (n_segments,);
        "share" - доля клиентов в каждом сегменте, форма (n_segments,);
        "profile" - средние значения признаков X по клиентам сегмента (в исходных
            единицах), форма (n_segments, n_features); для пустого сегмента -
            строка из np.nan.

    Пример:
        segment_summary(np.array([[10], [20], [60]]), np.array([0, 0, 2]), 3)
        -> {"size": [2, 0, 1], "share": [0.667, 0.0, 0.333], "profile": [[15.0], [nan], [60.0]]}
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    X = np.loadtxt(DATA / "features.csv", delimiter=",", skiprows=1, dtype=int)
    centers = np.loadtxt(DATA / "segments.csv", delimiter=",", skiprows=1, dtype=int)
    print("Z-score, первые 3 клиента:\n", scale_features(X, "zscore")[:3].round(3))
    for method in ("zscore", "minmax"):
        labels = assign_segments(X, centers, method)
        summary = segment_summary(X, labels, len(centers))
        print(method, "- размеры сегментов:", summary["size"])
        print("Профили:\n", summary["profile"].round(1))
