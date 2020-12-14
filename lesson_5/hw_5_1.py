#
with open("text_5_1.txt", "w") as my_obj:
    line = input('Вводите текст: ')
    while line:
        my_obj.writelines(line + "\n")
        line = input('Вводите текст: ')
        if not line:
            break


with open("text_5_1.txt") as my_obj:
    for element in my_obj:
        print(element)
