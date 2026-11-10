from task7 import simulate_month_revenue


def test_simulate_shape():
    revenues = simulate_month_revenue(n_sims=100, n_days=30, visitors=100, conversion=0.05, mean_check=1000, seed=1)
    assert revenues.shape == (100,)
