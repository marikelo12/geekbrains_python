month=int(input("Введите номер месяца: "))
season=('Зима','Весна', 'Лето', 'Осень')
if month==1 or month==2 or month==12:
    print(season[0])
elif month==3 or month==4 or month==5:
    print(season[1])
elif month==6 or month==7 or month==8:
    print(season[2])
elif month==9 or month==10 or month==11:
    print(season[3])
else:
    print("Время года не определено.")
