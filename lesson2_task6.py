lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for i in range(0, len(lst)):
    number = int(lst[i])
    if (number < 30) and (number % 3 == 0):
        print(number)
