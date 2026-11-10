import numpy as np
from task1 import top_k


def test_top_k_distinct():
    assert list(top_k(np.array([3, 10, 7, 1]), 2)) == [1, 2]
