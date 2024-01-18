var_1 = 37
var_2 = 99

print("Исходный вид: ", var_1, var_2)

# вариант 1
var_3 = var_2
var_2 = var_1
var_1 = var_3

print(var_1, var_2)

#вариант 2

var_1 = 37 + 99
var_2 = var_1 - 99
var_1 = var_1 - 37

print(var_1, var_2)