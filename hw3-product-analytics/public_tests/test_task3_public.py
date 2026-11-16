import pandas as pd
import pytest
from task3 import arpu


def test_arpu_simple():
    events = pd.DataFrame(
        {
            "user_id": ["a", "a", "b"],
            "event": ["app_open", "purchase", "app_open"],
            "event_date": pd.to_datetime(["2026-01-10", "2026-01-10", "2026-01-11"]),
            "amount": [float("nan"), 1000.0, float("nan")],
        }
    )
    assert arpu(events, "2026-01-01", "2026-01-31") == pytest.approx(500.0)
