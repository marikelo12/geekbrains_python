elements_list = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
while i < elements_list:
    my_list.append(input(f"Введите  значение элемента №{i+1}: "))
    i=i+1
print(f"Заданный список {my_list}")

element= 0
for x in range(len(my_list)//2):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(f"Измененный список {my_list}")