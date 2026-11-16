import pandas as pd
from task1 import load_orders

CSV = """invoice,line_no,stock_code,description,quantity,invoice_date,price,currency,customer_id,country,loaded_at
536365,1,85123A,WHITE HANGING HEART,6,25.03.2010 08:26,2.55,GBP,17850.0,United Kingdom,26.03.2010 03:00
C536366,1,22633,HAND WARMER UNION JACK,-6,26.03.2010 09:01,1.85,GBP,,United Kingdom,27.03.2010 03:00
"""


def test_load_orders_basic(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(CSV)
    df = load_orders(path)
    assert len(df) == 2
    assert df.loc[0, "invoice_date"] == pd.Timestamp("2010-03-25 08:26")
    assert df.loc[1, "quantity"] == -6
