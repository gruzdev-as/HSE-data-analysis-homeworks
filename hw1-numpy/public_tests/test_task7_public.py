import numpy as np
from task7 import minmax_scale


def test_minmax_scale_basic():
    X = np.array([[0, 10], [5, 20], [10, 30]])
    assert np.allclose(minmax_scale(X), [[0, 0], [0.5, 0.5], [1, 1]])
