import json

import pytest
from task10 import load_marketing

pytestmark = pytest.mark.bonus


def test_load_marketing_columns(tmp_path):
    path = tmp_path / "marketing.json"
    path.write_text(json.dumps([{"week": "2010-03-01", "spend": {"email": 10.0}, "manager": "Ann"}]))
    result = load_marketing(path)
    assert list(result.columns) == ["week", "channel", "spend"]
    assert result["spend"].tolist() == [10.0]
