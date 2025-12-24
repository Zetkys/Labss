a = int(input("Введите чсило: "))
for i in range(1, a + 1):
    print(i)

b = int(input("Введите первое число: "))
c = int(input("Введите второе число: "))
if b > c:
    print("Большее число: ", b)
elif b < c:
    print("Большее число: ", c)
if b == c:
    print("Числа равны")