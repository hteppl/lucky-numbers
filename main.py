# Написать функцию happy_numbers(n), которая возвращает список всех
# счастливых чисел в интервале от 1 до n.
# Число является счастливым, если для него выполняется следующая закономерность:
# 7^2=49 -> 4^2+9^2=97 -> 9^2+7^2=130 -> 1^2+3^2+0^2=10 -> 1^2+0^2=1
# (в конце остается единица)


import traceback


def happy_numbers(n):
    nums = list(range(1, n + 1))
    result = list()

    for element in nums:
        res = is_happy_number(element)

        while res != 1 and res != 4:
            res = is_happy_number(res)

        if res == 1:
            result.append(element)

    return result


def is_happy_number(n):
    res = 0

    while n > 0:
        rem = n % 10
        res = res + (rem * rem)
        n = n // 10

    return res


# Тесты
try:
    assert happy_numbers(10) == [1, 7, 10]
    assert happy_numbers(50) == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
    assert happy_numbers(100) == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
