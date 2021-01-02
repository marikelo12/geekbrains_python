with open('text_5_3.txt') as my_obj:
    zarpl = []
    pers = []
    for value in my_obj:
        element = value.split()
        plan = 20000
        if int(element[1]) < plan:
            pers.append(element[0])
        zarpl.append(int(element[1]))
    pers = ', '.join(pers)
    sred_zp = sum(zarpl) / len(zarpl)
    print(f'Меньше 20 тысяч рублей получают: {pers}.\nСредняя заработная плата составляет: {sred_zp} руб.')
