import pandas as pd
from task5 import funnel


def test_funnel_simple():
    events = pd.DataFrame(
        {
            "user_id": ["a", "a", "b"],
            "event": ["view_item", "purchase", "view_item"],
            "event_ts": pd.to_datetime(["2026-01-10 12:00", "2026-01-10 12:05", "2026-01-10 13:00"]),
        }
    )
    result = funnel(events, ["view_item", "purchase"])
    assert result["users"].tolist() == [2, 1]
