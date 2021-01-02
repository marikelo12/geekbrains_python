import json

with open('text_5_7.txt') as file:
    profit = {}
    prof = 0
    prof_aver = 0
    i = 0
    for line in file:
        name, firm, revenue, expense = line.split()
        profit[name] = int(revenue) - int(expense)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i > 0:
        prof_aver = round(prof / i)
        print(f'Средняя прибыль - {prof_aver}')
        print(f'Количество прибыльных фирм: {i}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    sr_profit = {'average_profit': prof_aver}
    itog_list = [profit, sr_profit]
    print(itog_list)

with open('text_5_7.json', 'w') as write_js:
    json.dump(itog_list, write_js)
    print(f'С данным содержимым создан Json-объект')
