import pandas as pd
from task1 import load_events


def test_load_events_columns_and_moscow_time(tmp_path):
    path = tmp_path / "events.csv"
    path.write_text(
        "event_id,user_id,event,event_ts,received_at,amount\n"
        "101,512345,app_open,2026-01-10T09:00:00Z,2026-01-10T09:00:02Z,\n"
        "102,512345,purchase,2026-01-10T09:05:00Z,2026-01-10T09:05:01Z,1500.0\n"
    )
    df = load_events(path)
    assert list(df.columns) == ["event_id", "user_id", "event", "event_ts", "received_at", "amount", "event_date"]
    assert df["event_ts"].iloc[0] == pd.Timestamp("2026-01-10 12:00:00")
