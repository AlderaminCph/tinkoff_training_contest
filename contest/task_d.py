"""
У Кости есть бумажка,
на которой написано n чисел.
Также у него есть возможность не больше, чем k раз,
взять любое число с бумажки,
после чего закрасить одну из старых цифр,
а на ее месте написать новую произвольную цифру.
На какое максимальное значение Костя сможет увеличить
сумму всех чисел на листочке?

Формат входных данных
В первой строке входного файла даны два целых числа
n, k — количество чисел на бумажке и ограничение на число операций.
 .
Во второй строке записано n чисел — числа на бумажке

Формат выходных данных
В выходной файл выведите одно число — максимальную
разность между конечной и начальной суммой.
"""


def get_maximum_difference_in_sum(
    digit_number: int, operation_number: int, digits: list[int]
) -> int:
    diffs = []
    for number in digits:
        weight = 1
        while number:
            digit = number % 10
            diffs.append((9 - digit) * weight)
            weight *= 10
            number //= 10
    diffs.sort(reverse=True)
    return sum(diffs[:operation_number])


if __name__ == "__main__":
    digit_number, operation_number = map(int, input().split())
    digits = list(map(int, input().split()))
    print(get_maximum_difference_in_sum(digit_number, operation_number, digits))
