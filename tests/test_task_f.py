import pytest

from contest.task_f import get_swap_elements


@pytest.mark.parametrize(
    ["number_of_students", "students_hight", "expected_result"],
    [(4, [2, 1, 4, 6], [-1, -1]), (2, [1, 2], [-1, -1]), (2, [2, 1], [1, 2])],
)
def test_get_swap_elements(number_of_students, students_hight, expected_result):
    result = get_swap_elements(number_of_students, students_hight)
    assert result == expected_result
