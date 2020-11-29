number=int(input("Введите число: "))
a=number%10
b=number//10
while b>0:
    if b%10>a:
        a=b%10
    b=b//10
print(a)
