import pandas as pd
from task3 import split_cancellations


def test_split_cancellations_basic():
    orders = pd.DataFrame({"invoice": ["100", "C101", "102"], "quantity": [1, -1, 2]})
    sales, cancellations = split_cancellations(orders)
    assert sales["invoice"].tolist() == ["100", "102"]
    assert cancellations["invoice"].tolist() == ["C101"]
