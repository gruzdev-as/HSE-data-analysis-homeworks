import pandas as pd
from task2 import remove_internal


def test_remove_internal():
    events = pd.DataFrame({"user_id": ["111111", "222222"], "event": ["app_open", "app_open"]})
    users = pd.DataFrame({"user_id": ["111111", "222222"], "channel": ["organic", "internal"]})
    assert remove_internal(events, users)["user_id"].tolist() == ["111111"]
