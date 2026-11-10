import numpy as np
from task9 import count_in_range


def test_count_in_range_inside():
    assert count_in_range(np.array([1, 5, 7, 20]), 2, 10) == 2
