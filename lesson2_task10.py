def bank(x, y):
    for i in range(1, y+1):
        x = x/100 * perc + x
    return x

perc = 10
x = int(input("Введите сумму вклада: "))
y = int(input("Введите количество лет: "))
bank(x, y)
print("Сумма в конце срока вклада: ", round(bank(x, y), 2))