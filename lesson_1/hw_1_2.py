time=int(input("Введите время в секундах: "))
hours=time//3600
minuts=time%3600//60
secunds=time%3600%60

print("Время: %02d:%02d:%02d" % (hours,minuts,secunds))