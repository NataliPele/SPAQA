def is_leap_year(year):
    return year % 4 == 0

year = int(input("Введите год: "))
is_leap_year(year)
print("Этот год високосный: ", is_leap_year(year))