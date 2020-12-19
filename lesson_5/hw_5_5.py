with open('text_5_5.txt', 'w') as my_obj:
    el = input('Введите необхоимые числа через пробел: ')
    my_obj.writelines(el)
    el_list = el.split()
    print(sum(map(int, el_list)))


