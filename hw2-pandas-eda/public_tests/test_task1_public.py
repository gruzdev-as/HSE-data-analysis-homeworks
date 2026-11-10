import pandas as pd
from task1 import load_orders, summary

CSV = """invoice,line_no,stock_code,description,quantity,invoice_date,price,currency,customer_id,country,loaded_at
536365,1,85123A,WHITE HANGING HEART,6,25.03.2010 08:26,2.55,GBP,17850.0,United Kingdom,26.03.2010 03:00
536365,2,71053,WHITE METAL LANTERN,6,25.03.2010 08:26,3.39,GBP,17850.0,United Kingdom,26.03.2010 03:00
536366,1,22633,HAND WARMER UNION JACK,6,26.03.2010 09:01,1.85,GBP,,United Kingdom,27.03.2010 03:00
"""


def test_load_orders_basic(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(CSV)
    df = load_orders(path)
    assert len(df) == 3
    assert df.loc[0, "invoice_date"] == pd.Timestamp("2010-03-25 08:26")
    assert df.loc[0, "quantity"] == 6


def test_summary_counts(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(CSV)
    result = summary(load_orders(path))
    assert result["n_rows"] == 3
    assert result["n_invoices"] == 2
