def my_func(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError as err:
        print("На ноль делить нельзя!", err)


print(my_func(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: "))))







