import pytest

from contest.task_b import get_minimum_number_of_cuts


@pytest.mark.parametrize(
    ["number_of_peaces", "expected_result"],
    [(1, 0), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 3), (8, 3)],
)
def test_get_minimum_number_of_cuts(number_of_peaces, expected_result):
    result = get_minimum_number_of_cuts(number_of_peaces)
    assert result == expected_result
