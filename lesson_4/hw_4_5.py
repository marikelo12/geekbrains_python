from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


print(f'Результат: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
