class NewException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]


def division(a, b):
    if not b:
        raise NewException('Делить на ноль нельзя', [1, 2, 3])
    return a / b


try:
    print(division(1, 0))
except NewException as err:
    print(type(err), err)



