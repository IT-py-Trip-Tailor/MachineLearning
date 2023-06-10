import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Загрузка данных
data = pd.read_csv('tour_data.csv')

# Предобработка данных
label_encoders = {}  # Создаем словарь для хранения LabelEncoder для каждого столбца
cols_to_encode = ['Откуда', 'Куда', 'Тип тура', 'Цель тура', 'Трансфер',
                  'Тип размещения', 'Питание', 'Активности', 'Язык гида', 'Маршрут']

for col in cols_to_encode:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  # Сохраняем LabelEncoder для этого столбца

columns_to_drop = ['Возраст', 'Звезды отеля', 'Маршрут', 'Размер группы']
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
    'Трансфер': 'автобус',
    'Тип размещения': 'кемпинг',
    'Питание': 'полный пансион',
    'Активности': 'сафари',
    'Язык гида': 'испанский'
}

# Преобразование пользовательских данных
for col, value in user_input.items():
    if col in label_encoders:  # Используем LabelEncoder, соответствующий этому столбцу
        user_input[col] = label_encoders[col].transform([value])[0]

user_data = scaler.transform(pd.DataFrame([user_input]))

# KNN алгоритм
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(scaled_data)
_, indices = knn.kneighbors(user_data)

# Вывод результатов
recommended_tours = data.iloc[indices[0]]
print(recommended_tours)
