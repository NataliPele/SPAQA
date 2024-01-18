def month_to_season(i):
    if (i == 1) or (i == 2) or (i == 12):
        print("Время года зима")
    elif (i == 3) or (i == 4) or (i == 5):
        print("Время года весна")
    elif (i == 6) or (i == 7) or (i == 8):
        print("Время года лето")
    elif (i == 9) or (i == 10) or (i == 11):
        print("Время года осень")
    else:
        print("Ой, такого месяца нет:(")

i = int(input("Введите номер месяца: "))
month_to_season(i)