import numpy as np
from task1 import pct_change, to_weeks


def test_to_weeks_shape():
    assert to_weeks(np.arange(21)).shape == (3, 7)


def test_pct_change_basic():
    assert np.allclose(pct_change(np.array([100, 150, 75])), [0.5, -0.5])
