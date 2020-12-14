# def sum_2(arg1, arg2, arg3):
#     if arg1 >= arg3 and arg2 >= arg3:
#         return arg1 + arg2
#     elif arg2 > arg1 and arg3 > arg1:
#         return arg2 + arg3
#     else:
#         return arg3 + arg1
#
#
# print(
#     f'Результат: {sum_2(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: ")), int(input("Введите 3-е число: ")))}')


def sum_of_max(*args):
    return sum(args) - min(args)


print(sum_of_max(1, 3, 4, 5))
