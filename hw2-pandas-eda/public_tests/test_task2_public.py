import pandas as pd
from task2 import normalize_country


def test_normalize_country_alias():
    assert normalize_country(pd.Series(["UK", "France"])).tolist() == ["United Kingdom", "France"]
