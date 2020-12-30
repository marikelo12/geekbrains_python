class NewException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]

def division(x):
    if not x.isdigit():
        raise NewException('Введено не число', [1, 2, 3])
    return x


my_list = []
my_str = ''
while 'stop' not in my_str:
    try:
        my_str = input('Введите число или "stop": ')
        my_list.append(division(my_str))
        print(my_list)

    except NewException as err:
        print(type(err), err)

else:
    print(f'Вы завершили программу \nРезультат: {my_list}')