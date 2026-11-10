import pytest
from task10 import simulate_funnel


@pytest.mark.bonus
def test_simulate_funnel_shape():
    assert simulate_funnel(n_impressions=1000, p_click=0.1, p_buy=0.2, n_sims=50, seed=0).shape == (50, 3)
