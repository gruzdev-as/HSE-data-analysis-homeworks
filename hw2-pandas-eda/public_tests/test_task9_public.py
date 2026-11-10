import pandas as pd
from task9 import count_buyers


def test_count_buyers_no_repeats():
    sales = pd.DataFrame({"customer_id": pd.array([1, 2, 3], dtype="Int64")})
    assert count_buyers(sales) == 3
