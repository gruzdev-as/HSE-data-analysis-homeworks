import pandas as pd
from task5 import to_gbp


def test_to_gbp_gbp_unchanged():
    orders = pd.DataFrame(
        {"price": [2.0, 4.0], "currency": ["GBP", "GBP"], "invoice_date": pd.to_datetime(["2010-07-01", "2010-07-02"])}
    )
    fx = pd.DataFrame(
        {"date": pd.to_datetime(["2010-07-01", "2010-07-02"]), "currency": ["EUR", "EUR"], "units_per_gbp": [1.2, 1.2]}
    )
    assert to_gbp(orders, fx)["price_gbp"].tolist() == [2.0, 4.0]
