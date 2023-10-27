# Требуется вычислить, сколько раз
# встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

# print(list_1.count(k))

# -------------------------------------------------------------------------

# Требуется найти в массиве list_1 самый близкий
# по величине элемент к заданному числу k и вывести его.

# Пример:

# list_1 = [1, -4, 3, 7, 8, 9, 2]
# k = -3
# min_range = abs(k - list_1[0])
# min_range_number = list_1[0]
# for item in list_1:
#     current_range = abs(k - item)
#     # print(current_range, end = " ")
#     if current_range < min_range:
#         min_range = current_range
#         min_range_number = item
# # print("\n")
# # print(min_range)
# print(min_range_number)

# -------------------------------------------------

list_1 = {1: "AEIOULNSTRАВЕИНОРСТ",
          2: "DGДКЛМПУ",
          3: "BCMPБГЁЬЯ",
          4: "FHVWYЙЫ",
          5: "KЖЗХЦЧ",
          8: "JXШЭЮ",
          10: "QZФЩЪ"}

word = 'ноутбук'
sum_letters = 0

for item in word.upper():
    for key, value in list_1.items():
        if item in value:
            sum_letters += key
            break
print(sum_letters)