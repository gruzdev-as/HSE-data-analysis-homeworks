import pandas as pd
from task6 import cohort_report


def test_cohort_report_sizes():
    users = pd.DataFrame(
        {"user_id": ["a", "b", "c"], "signup_date": pd.to_datetime(["2026-01-05", "2026-01-07", "2026-01-12"])}
    )
    events = pd.DataFrame(
        {
            "user_id": ["a", "b", "c"],
            "event": ["app_open"] * 3,
            "event_date": pd.to_datetime(["2026-01-05", "2026-01-07", "2026-01-12"]),
            "amount": [float("nan")] * 3,
        }
    )
    assert cohort_report(events, users, "2026-01-25")["sizes"].tolist() == [2, 1]
