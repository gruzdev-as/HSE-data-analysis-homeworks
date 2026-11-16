import pandas as pd
import pytest
from task7 import channel_report


def test_channel_report_single_channel():
    users = pd.DataFrame({"user_id": ["a", "b"], "channel": ["ads_search", "ads_search"]})
    events = pd.DataFrame({"user_id": ["a"], "event": ["purchase"], "amount": [3000.0]})
    spend = pd.DataFrame({"week": pd.to_datetime(["2026-01-05"]), "channel": ["ads_search"], "spend": [1000.0]})
    assert channel_report(users, events, spend).loc["ads_search", "cac"] == pytest.approx(500.0)
