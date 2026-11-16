"""
Задание 9*. Сжатие картинки через SVD.

Вы пишете функции, которые сжимают картинку: вместо всех пикселей хранят только
k главных компонент SVD. Работаете с img - чёрно-белой картинкой, форма
(height, width), dtype uint8, значения яркости 0..255.
"""

import numpy as np


def compress_image(img: np.ndarray, k: int) -> np.ndarray:
    """
    Сожмите картинку: постройте её приближение ранга k через SVD (оставьте
    k наибольших сингулярных чисел). Верните картинку той же формы с dtype uint8:
    значения округлите до целых, они должны лежать в 0..255.
    Если k больше min(height, width), используйте min(height, width).
    """
    # TODO: ваш код здесь
    ...


def compression_ratio(shape: tuple[int, int], k: int) -> float:
    """
    Посчитайте, во сколько раз меньше чисел нужно хранить для приближения ранга k,
    чем для исходной картинки: h * w / (k * (h + w + 1)). Ограничьте k так же,
    как в compress_image.

    Пример:
        compression_ratio((100, 200), 10) -> 6.644...
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    from pathlib import Path

    DATA = Path(__file__).parent / "data"
    import matplotlib.pyplot as plt

    img = np.load(DATA / "image.npy")
    ks = [5, 20, 50]
    fig, axes = plt.subplots(1, len(ks) + 1, figsize=(16, 4))
    axes[0].imshow(img, cmap="gray", vmin=0, vmax=255)
    axes[0].set_title("Оригинал")
    for ax, k in zip(axes[1:], ks):
        ax.imshow(compress_image(img, k), cmap="gray", vmin=0, vmax=255)
        ax.set_title(f"k={k}, сжатие в {compression_ratio(img.shape, k):.1f} раз")
    for ax in axes:
        ax.axis("off")
    plt.show()
