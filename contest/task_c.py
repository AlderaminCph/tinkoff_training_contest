"""
У Кати насыщенный день на работе.
Ей надо передать n разных договоров коллегам.
Все встречи происходят на разных этажах,
а между этажами можно перемещаться только по лестничным пролетам —
считается, что это улучшает физическую форму сотрудников.
Прохождение каждого пролета занимает ровно 1 минуту.
Сейчас Катя на парковочном этаже,
планирует свой маршрут.
Коллег можно посетить в любом порядке,
но один из них покинет офис через t минут.
С парковочного этажа лестницы нет — только лифт,
на котором можно подняться на любой этаж.
В итоге план Кати следующий:

1. Подняться на лифте на произвольный этаж.
Считается, что лифт поднимается на любой этаж за 0 минут.
2. Передать всем коллегам договоры, перемещаясь между этажами по лестнице.
Считается, что договоры на этаже передаются мгновенно.
3. В первые t минут передать договор тому коллеге, который планирует уйти.
4. Пройти минимальное количество лестничных пролетов.
Помогите Кате выполнить все пункты ее плана.

Формат входных данных
В первой строке вводятся целые положительные числа n и t —
количество сотрудников и время,
когда один из сотрудников покинет офис (в минутах).
В следующей строке n чисел — номера этажей, на которых находятся сотрудники.
Все числа различны и по абсолютной величине не превосходят 100.
Номера этажей даны в порядке возрастания.
В следующей строке записан номер сотрудника, который уйдет через t минут.

Формат выходных данных
Выведите одно число —
минимально возможное число лестничных пролетов,
которое понадобится пройти Кате.

"""


def get_minimum_number_of_stair_flights(
    number_employes: int, time: int, floors_number: list[int], employee: int
) -> int:
    floor_of_employee = floors_number[employee - 1]
    time_to_elevate = floor_of_employee - floors_number[0]
    number_of_flights = 0
    if time_to_elevate > time:
        # raising to employee floor
        if floors_number[-1] - floor_of_employee < time_to_elevate:
            # rasing up
            number_of_flights = (
                floors_number[-1]
                - floor_of_employee
                + floors_number[-1]
                - floors_number[0]
            )
        else:
            # down
            number_of_flights = time_to_elevate - floors_number[0] + floors_number[-1]
    else:
        # starting with first floor
        number_of_flights = floors_number[-1] - floors_number[0]
    return number_of_flights


if __name__ == "__main__":
    number_employes, time = map(int, input().split())
    floors_number = map(int, input().split())
    employee = int(input())
    print(
        get_minimum_number_of_stair_flights(
            number_employes, time, floors_number, employee
        )
    )
