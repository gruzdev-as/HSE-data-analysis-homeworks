import pandas as pd
from task8 import daily_revenue


def test_daily_revenue_consecutive_days():
    sales = pd.DataFrame(
        {
            "quantity": [1, 2, 1],
            "price": [10.0, 5.0, 3.0],
            "invoice_date": pd.to_datetime(["2010-05-03 10:00", "2010-05-03 15:00", "2010-05-04 09:00"]),
        }
    )
    result = daily_revenue(sales)
    assert result.tolist() == [20.0, 3.0]
