import pytest

from contest.task_e import get_max_number_of_different_tests


@pytest.mark.parametrize(
    ["left", "right", "expected_result"],
    [(4, 7, 4), (11, 100, 9)],
)
def test_get_max_number_of_different_tests(left, right, expected_result):
    result = get_max_number_of_different_tests(left, right)
    assert result == expected_result
