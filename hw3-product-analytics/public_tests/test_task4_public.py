import pandas as pd
from task4 import audience_report


def test_audience_report_dau():
    events = pd.DataFrame(
        {"user_id": ["a", "b", "a"], "event_date": pd.to_datetime(["2026-01-10", "2026-01-10", "2026-01-11"])}
    )
    assert audience_report(events)["dau"].tolist() == [2, 1]
