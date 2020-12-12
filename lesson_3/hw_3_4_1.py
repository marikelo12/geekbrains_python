def my_func(x, y):
    res = 1
    count = 0
    while count < y:
        res = res * x
        count += 1
        if y == 0:
            res = 1
    return 1 / res


print(f"Результат: {my_func(float(input('Введите число: ')), abs(int(input('Введите отрицательную степень: '))))}")

