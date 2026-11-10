import numpy as np
from task2 import daily_revenue


def test_daily_revenue_basic():
    sales = np.array([[1, 2, 0], [3, 0, 1]])
    prices = np.array([10.0, 100.0])
    assert np.allclose(daily_revenue(sales, prices), [310, 20, 100])
