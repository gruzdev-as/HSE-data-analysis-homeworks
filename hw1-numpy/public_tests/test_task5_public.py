import numpy as np
from task5 import nearest_point


def test_nearest_point_basic():
    customers = np.array([[0.0, 0.0], [10.0, 10.0], [9.0, 0.0]])
    points = np.array([[1.0, 1.0], [10.0, 9.0]])
    assert list(nearest_point(customers, points)) == [0, 1, 0]
