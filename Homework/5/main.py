# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# def sum_num(num_1, num_2):
#     if num_2 == 0:
#         return 1
#     return num_1 * sum_num(num_1, num_2 - 1)

# a, b = 3, 3

# print(sum_num(a,b))

# ---------------------------------------------------------------------------

# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

def sum(a,b):
    if b == 0:
        return a
    if b > 0:
        return sum(a + 1, b - 1)
    else:
        return sum(a - 1, b + 1)

a = -10
b = -5

print(sum(a, b))