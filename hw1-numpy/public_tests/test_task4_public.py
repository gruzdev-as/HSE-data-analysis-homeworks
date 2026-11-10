import numpy as np
from task4 import weekly_report


def test_weekly_report_starts_on_monday():
    daily = np.arange(14, dtype=float).reshape(1, 14)
    report = weekly_report(daily, 0)
    assert report["weeks"].shape == (1, 2, 7)
    assert np.allclose(report["profile"], [[3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]])
