from itertools import count, cycle

n = int(input("Введите начальное число: "))
c = int(input("Введите конечное число: "))
my_list = []

for el in count(n):
    if el > c:
        break
    else:
        print(el)
        my_list.append(el)
        el += 1
print(my_list)

x = int(input("Сколько элементов вывести из списка?: "))
c = 0
for el in cycle(my_list):
    if c < x:
        print(el)
        c += 1

