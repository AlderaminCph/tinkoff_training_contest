import pytest

from contest.task_a import get_internet_expenses


@pytest.mark.parametrize(
    ["tariff_cost", "tariff_size", "extra_price", "traffic_size", "expected_result"],
    [(100, 10, 12, 15, 160), (100, 10, 12, 1, 100)],
)
def test_get_internet_expenses(
    tariff_cost, tariff_size, extra_price, traffic_size, expected_result
):
    result = get_internet_expenses(tariff_cost, tariff_size, extra_price, traffic_size)
    assert result == expected_result
