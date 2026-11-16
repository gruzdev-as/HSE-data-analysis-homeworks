import pandas as pd
from task5 import country_report


def test_country_report_revenue():
    sales = pd.DataFrame(
        {
            "invoice": ["1", "2"],
            "quantity": [1, 2],
            "price": [10.0, 10.0],
            "customer_id": pd.array([1, 2], dtype="Int64"),
            "country": ["France", "Germany"],
            "invoice_date": pd.to_datetime(["2010-05-01", "2010-05-02"]),
        }
    )
    report = country_report(sales)
    assert report.loc["Germany", "revenue"] == 20.0
    assert report.loc["France", "revenue"] == 10.0
