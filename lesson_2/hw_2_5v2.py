my_list = [7, 5, 3, 3, 2]
new_el = int(input("Введите число рейтинга: "))
while new_el != 666:
    x = new_el in my_list
    if x == True:
        a = my_list.index(new_el)
        b = my_list.count(new_el)
        my_list.insert(a + b, new_el)
        print(my_list)
    elif x == False:
        for el in range(len(my_list)):
            if my_list[-1] > new_el:
                my_list.append(new_el)
                print(my_list)
            elif my_list[0] < new_el:
                my_list.insert(0, new_el)
                print(my_list)
            elif my_list[el] > new_el and my_list[el + 1] < new_el:
                my_list.insert(el + 1, new_el)
                print(my_list)
    new_el = int(input("Введите новое число рейтинга (для выхода введите - 666): "))
