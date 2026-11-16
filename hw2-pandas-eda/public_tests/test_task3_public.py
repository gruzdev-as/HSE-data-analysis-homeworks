import pandas as pd
from task3 import revenue_by_country


def test_revenue_by_country_basic():
    sales = pd.DataFrame(
        {
            "invoice": ["1", "2", "3"],
            "quantity": [1, 2, 1],
            "price": [10.0, 10.0, 5.0],
            "country": ["France", "Germany", "France"],
        }
    )
    result = revenue_by_country(sales)
    assert result["Germany"] == 20.0
    assert result["France"] == 15.0
