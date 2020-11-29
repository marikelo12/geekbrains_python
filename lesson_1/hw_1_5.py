revenu=int(input("Введите Вашу выручку: "))
losse= int(input("Введите Ваши расходы: "))
proffit=revenu-losse

if proffit>0:
    print(f"Ваша прибыль составила {proffit}")
    rentable = proffit / revenu * 100
    print(f"Ваша рентабельность сосавляет {rentable} %")
    personal=int(input("Введите количество сорудников: "))
    person_proffit =proffit/personal
    print(f"Средняя прибыль на 1 сотруника составляет: {person_proffit}")
elif proffit<0:
    print(f"Ваши потери составили: {proffit}")
else:
    print("У Вас нулевая прибыль")