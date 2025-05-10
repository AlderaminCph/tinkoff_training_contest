import pytest

from contest.task_c import get_minimum_number_of_stair_flights


@pytest.mark.parametrize(
    ["number_employes", "time", "floors_number", "employee", "expected_result"],
    [(5, 5, [1, 4, 9, 16, 25], 2, 24), (6, 4, [1, 2, 3, 6, 8, 25], 5, 31)],
)
def test_get_minimum_number_of_stair_flights(
    number_employes, time, floors_number, employee, expected_result
):
    result = get_minimum_number_of_stair_flights(
        number_employes, time, floors_number, employee
    )
    assert result == expected_result
