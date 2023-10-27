# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = "a a a b c a a d c d d"
list_1 = text.split()
print(list_1)
dict_1 = dict()
for letter in list_1:
    if letter not in dict_1:
        dict_1[letter] = 0
    else:
        dict_1[letter] += 1
        print(f"{letter}_{dict_1[letter]}", end=" ")

# 2

text = "a a a b c a a d c d d"
dict_1 = dict()
for letter in text.split():
    print(letter, end=" ") if letter not in dict_1 else print(f"{letter}_{dict_1[letter]}", end=" ")
    dict_1[letter] = dict_1.get(letter, 0) + 1

# ----------------------------------------------------------------------------

# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним пробелом.
# Определите, сколько различных слов содержится в этом тексте.
# 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea "
        "shells on the sea shore I'm sure that the shells are sea shore shells")
set_1 = set(text.lower().split())
print(f"Количество слов: {len(set_1)}")

# ----------------------------------------------------------------------------------

# Задача – «На вход программе подаются натуральные числа,
# как только пользователь введёт 0 ввод прекращается.
# Вывести наибольший элемент получившейся последовательности». 

# Есть два кода с ошибками, нужно определить  где ошибок меньше.

# Ваня:
# 
# n = int(input())
# max_number = n # 1 - max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number < n: # 2 - if max_number > n:
#         max_number = n
# print(max_number) # в итоге 2 ошибки
#
# Петя:
# 
# n = int(input())
# max_number = -1
# while n:                    # 1 - while n < 0:
#     if max_number < n:
#         max_number = n      # 2 - n = max_number
#     n = int(input())        # 3 - перенос строки за условие if
# print(max_number)           # 4 -  print(n)


