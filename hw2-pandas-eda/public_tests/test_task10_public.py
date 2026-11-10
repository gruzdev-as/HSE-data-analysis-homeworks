import pandas as pd
import pytest
from task10 import to_gbp_asof

pytestmark = pytest.mark.bonus


def test_to_gbp_asof_same_day():
    orders = pd.DataFrame({"price": [2.4], "currency": ["EUR"], "invoice_date": pd.to_datetime(["2010-07-01 12:00"])})
    fx = pd.DataFrame({"date": pd.to_datetime(["2010-07-01"]), "currency": ["EUR"], "units_per_gbp": [1.2]})
    assert to_gbp_asof(orders, fx)["price_gbp"].iloc[0] == pytest.approx(2.0)
