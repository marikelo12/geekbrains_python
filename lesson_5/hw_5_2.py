with open('text_5_2.txt') as my_obj:
    lines = len(my_obj.readlines())
    print(f'Количество строк в файле - {lines}')

with open('text_5_2.txt') as my_obj:
    lines = my_obj.readlines()

with open('text_5_2.txt') as my_obj:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print(f'В строке {index + 1} находится {number_of_words} слова.')
