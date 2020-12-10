sum_res = 0
x = True
while x:
    element = input('Введите числа или $ для выхода: ').split()
    res = 0
    for el in range(len(element)):
        if element[el] == "$":
            x = False
        else:
            res = res + int(element[el])
    sum_res = sum_res + res
    print(f'Промежуточная сумма: {sum_res}')
print(f'Конечная сумма: {sum_res}')
