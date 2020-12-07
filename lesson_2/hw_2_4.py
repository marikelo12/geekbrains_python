my_str=str(input("Введит строку: "))
my_list=list(my_str.split( ))
for x,el in enumerate(my_list,1):
        print(f"{x}. {el[0:10]}")