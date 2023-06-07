import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Загрузка данных
data = pd.read_csv('tour_data.csv')

# Предобработка данных
le = LabelEncoder()
data['Откуда'] = le.fit_transform(data['Откуда'])
data['Куда'] = le.fit_transform(data['Куда'])
data['Тип тура'] = le.fit_transform(data['Тип тура'])
data['Цель тура'] = le.fit_transform(data['Цель тура'])
data['Трансфер'] = le.fit_transform(data['Трансфер'])
data['Тип размещения'] = le.fit_transform(data['Тип размещения'])
data['Питание'] = le.fit_transform(data['Питание'])
data['Активности'] = le.fit_transform(data['Активности'])
data['Язык гида'] = le.fit_transform(data['Язык гида'])

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Ввод данных пользователем
user_input = {
    'Откуда': 'Санкт-Петербург',
    'Куда': 'Москва',
    'Бюджет': 50000,
    'Тип тура': 'обучение',
    'Цель тура': 'учеба',
    'Трансфер': 'автобус',
    'Тип размещения': 'кемпинг',
    'Питание': 'полный пансион',
    'Активности': 'сафари',
    'Язык гида': 'испанский'
}

# Преобразование пользовательских данных
for col, value in user_input.items():
    if col in le.classes_:
        user_input[col] = le.transform([value])[0]

user_data = scaler.transform(pd.DataFrame([user_input]))

# KNN алгоритм
knn = NearestNeighbors(n_neighbors=5, metric='manhattan')
knn.fit(scaled_data)
_, indices = knn.kneighbors(user_data)

# Вывод результатов
recommended_tours = data.iloc[indices[0]]
print(recommended_tours)
