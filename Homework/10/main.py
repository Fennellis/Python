import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print(data.head())

# Тип данных
TYPE_OF_DATA = int

# Вариант 1
new_data_1 = pd.get_dummies(data, dtype=TYPE_OF_DATA)

print(new_data_1.head())


# Вариант 2
new_data_2 = pd.DataFrame(data, columns=['human', 'robot'])

for i in data.index:
    if data.at[i, 'whoAmI'] == 'robot':
        new_data_2.at[i, 'robot'] = 1
        new_data_2.at[i, 'human'] = 0
    else:
        new_data_2.at[i, 'human'] = 1
        new_data_2.at[i, 'robot'] = 0

new_data_2 = new_data_2.astype(TYPE_OF_DATA)
print(new_data_2.head())