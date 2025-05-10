import pytest

from contest.task_d import get_maximum_difference_in_sum


@pytest.mark.parametrize(
    ["digit_number", "operation_number", "digits", "expected_result"],
    [(5, 2, [1, 2, 1, 3, 5], 16), (3, 1, [99, 5, 85], 10), (1, 10, [9999], 0)],
)
def test_get_maximum_difference_in_sum(
    digit_number, operation_number, digits, expected_result
):
    result = get_maximum_difference_in_sum(digit_number, operation_number, digits)
    assert result == expected_result
