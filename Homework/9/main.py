# Дан файл california_housing_train.csv.
# Определить среднюю стоимость дома,
# где количество людей от 0 до 500 (population)
# и сохранить ее в переменную avg.
# Используйте модуль pandas.

# import pandas as pd

# PATH = 'california_housing_train.csv'

# df = pd.read_csv(PATH, sep=',')

# print(df)

# temp = df[df['population'] <= 500]['median_house_value'].mean()

# print(temp)


# ----------------------------------------------------------------------

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households"
# в зоне минимального значения переменной "population"
# и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

# import pandas as pd

# PATH = 'california_housing_train.csv'

# df = pd.read_csv(PATH, sep=',')

# temp = df[df['population'] == df['population'].min()]['households'].max()

# print(temp)