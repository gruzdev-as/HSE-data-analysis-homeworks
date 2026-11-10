import pandas as pd
from task2 import add_line_total, top_products


def make_orders():
    return pd.DataFrame(
        {
            "invoice": ["1", "1", "2"],
            "stock_code": ["A", "B", "A"],
            "quantity": [2, 1, 3],
            "price": [10.0, 5.0, 10.0],
            "invoice_date": pd.to_datetime(["2010-05-01 10:00", "2010-05-01 10:00", "2010-05-02 11:00"]),
        }
    )


def test_add_line_total():
    assert add_line_total(make_orders())["line_total"].tolist() == [20.0, 5.0, 30.0]


def test_top_products_first():
    top = top_products(make_orders(), 1)
    assert list(top.index) == ["A"]
    assert top.iloc[0] == 50.0
