try:
    def my_func(arg1, arg2):
        return arg1 / arg2


    print(my_func(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: "))))
except ZeroDivisionError as err:
    print("На ноль делить нельзя!", err)






