import numpy as np
from task5 import scale_features


def test_minmax_basic():
    X = np.array([[0, 10], [5, 20], [10, 30]])
    assert np.allclose(scale_features(X, "minmax"), [[0, 0], [0.5, 0.5], [1, 1]])
