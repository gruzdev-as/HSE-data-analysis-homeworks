import pandas as pd
from task4 import normalize_country


def test_normalize_country_alias():
    result = normalize_country(pd.Series(["UK", "France"]))
    assert result.tolist() == ["United Kingdom", "France"]
