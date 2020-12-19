from itertools import count
from math import factorial


def my_func():
    for elem in count(1):
        yield factorial(elem)


f = int(input("Введите число подсчета факториала: "))
c = 0
for el in my_func():
    if c < f:
        print(el)
        c += 1
    else:
        break
