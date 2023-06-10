import pandas as pd

# Загрузите данные
df = pd.read_csv('tour_data.csv')

# Удалите столбец 'Даты'
df = df.drop('Даты', axis=1)

# Сохраните DataFrame обратно в тот же CSV-файл
df.to_csv('tour_data.csv', index=False)

# Проверьте изменения
print(df.head())
