import numpy as np
from task3 import average_check


def test_average_check_clean():
    assert average_check(np.array([100.0, 200.0, 600.0])) == 300.0
