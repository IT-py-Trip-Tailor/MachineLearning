import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Загрузка данных
data = pd.read_csv('tour_data.csv')

# Предобработка данных
label_encoders = {}
cols_to_encode = ['Откуда', 'Куда', 'Тип тура', 'Цель тура', 'Трансфер']

for col in cols_to_encode:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

columns_to_drop = ['Возраст', 'Звезды отеля', 'Маршрут', 'Размер группы', 'Тип размещения', 'Питание', 'Активности', 'Язык гида']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Ввод данных пользователем
user_input = {
    'Откуда': 'Санкт-Петербург',
    'Куда': 'Москва',
    'Бюджет': 50000,
    'Тип тура': 'обучение',
    'Цель тура': 'учеба',
    'Трансфер': 'автобус'
}

# Преобразование пользовательских данных
for col, value in user_input.items():
    if col in label_encoders:
        if value in label_encoders[col].classes_:  # Если значение присутствует в данных обучения
            user_input[col] = label_encoders[col].transform([value])[0]
        else:  # Если значение отсутствует в данных обучения
            print(f"Упс! Нам неизвестно значение '{value}' для {col}.")
            user_input[col] = -1

user_data = scaler.transform(pd.DataFrame([user_input]))

# KNN алгоритм
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(scaled_data)
_, indices = knn.kneighbors(user_data)

# Вывод результатов без первой строки и без заголовков столбцов
recommended_tours = data.iloc[indices[0]][1:]
recommended_tours_html = recommended_tours.to_html(header=False)
print(recommended_tours_html)
