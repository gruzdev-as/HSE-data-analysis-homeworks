import numpy as np
from task6 import basket_totals


def test_basket_totals_no_discount():
    baskets = np.array([[1, 0, 2], [0, 3, 0]])
    prices = np.array([10.0, 20.0, 5.0])
    assert np.allclose(basket_totals(baskets, prices, np.zeros(3)), [20, 60])
