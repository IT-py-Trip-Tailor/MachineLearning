import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

# Загрузка данных из CSV-файла
tour_data = pd.read_csv("tour_data.csv")

# Подготовка данных для обучения
le = LabelEncoder()

tour_data_encoded = tour_data.copy()
tour_data_encoded['Откуда'] = le.fit_transform(tour_data['Откуда'])
tour_data_encoded['Куда'] = le.fit_transform(tour_data['Куда'])
tour_data_encoded['Тип тура'] = le.fit_transform(tour_data['Тип тура'])
tour_data_encoded['Цель тура'] = le.fit_transform(tour_data['Цель тура'])
tour_data_encoded['Трансфер'] = le.fit_transform(tour_data['Трансфер'])

# Обучение модели KNN
X = tour_data_encoded[['Откуда', 'Куда', 'Бюджет', 'Тип тура', 'Цель тура', 'Трансфер']].values
knn = NearestNeighbors(n_neighbors=5, algorithm='auto', metric='euclidean').fit(X)

print("Введите предпочтения для вашего тура:")

from_location = input("Откуда (например, Москва): ")
to_location = input("Куда (например, Санкт-Петербург): ")
budget = int(input("Бюджет (например, 50000): "))
tour_type = input("Тип тура (например, отдых): ")
travel_purpose = input("Цель тура (например, культурный обмен): ")
transfer = input("Трансфер (например, самолет): ")

# Кодирование предпочтений пользователя
user_input = [
    le.fit(tour_data['Откуда']).transform([from_location])[0],
    le.fit(tour_data['Куда']).transform([to_location])[0],
    budget,
    le.fit(tour_data['Тип тура']).transform([tour_type])[0],
    le.fit(tour_data['Цель тура']).transform([travel_purpose])[0],
    le.fit(tour_data['Трансфер']).transform([transfer])[0]
]

# Получение рекомендаций
distances, indices = knn.kneighbors([user_input])

print("\nРекомендованные туры:")
for index in indices[0]:
    recommended_tour = tour_data.iloc[index]
    if recommended_tour['Откуда'] == from_location and recommended_tour['Куда'] == to_location:
        print(recommended_tour)
