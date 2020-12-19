from sys import argv

_, hours, time, bonus = argv


def my_func(hours, time, bonus):
    return hours * time + bonus


print(f"Выплата будет сосавлять:{my_func(int(hours), int(time), int(bonus))} рублей")



