import numpy as np
from task6 import similarities


def test_similarities_basic():
    ratings = np.array([[1, 0], [2, 0], [0, 3]])
    assert np.allclose(similarities(ratings, 0), [1.0, 1.0, 0.0])
