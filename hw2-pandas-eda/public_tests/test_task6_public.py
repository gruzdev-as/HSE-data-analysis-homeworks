import pandas as pd
from task6 import latest_profiles


def test_latest_profiles_single_rows():
    customers = pd.DataFrame(
        {
            "customer_id": [2, 1],
            "email": ["b@mail.com", "a@mail.com"],
            "segment": ["retail", "wholesale"],
            "signup_date": pd.to_datetime(["2010-01-01", "2010-01-02"]),
            "updated_at": pd.to_datetime(["2010-02-01", "2010-02-02"]),
        }
    )
    assert latest_profiles(customers)["customer_id"].tolist() == [1, 2]
