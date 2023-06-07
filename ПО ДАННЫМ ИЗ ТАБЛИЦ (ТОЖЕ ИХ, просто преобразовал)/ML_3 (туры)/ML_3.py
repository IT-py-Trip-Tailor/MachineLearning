import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Загрузка данных
data = pd.read_csv('tour_data.csv')

# Предобработка данных
data[['Дата начала', 'Дата окончания']] = data['Даты'].str.split(' - ', expand=True)
data['Дата начала'] = pd.to_datetime(data['Дата начала'], format='%Y-%m-%d')
data['Дата окончания'] = pd.to_datetime(data['Дата окончания'], format='%Y-%m-%d')
data.drop(columns=['Даты'], inplace=True)

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
scaled_data = scaler.fit_transform(data.drop(columns=['Дата начала', 'Дата окончания']))

# Ввод данных пользователем
print("Введите предпочтения для вашего тура:")

from_location = input("Откуда (например, Москва): ")
to_location = input("Куда (например, Санкт-Петербург): ")
budget = int(input("Бюджет (например, 50000): "))
tour_type = input("Тип тура (например, отдых): ")
travel_purpose = input("Цель тура (например, культурный обмен): ")
transfer = input("Трансфер (например, самолет): ")
accommodation = input("Тип размещения (например, кемпинг): ")
meal_plan = input("Питание (например, полный пансион): ")
activities = input("Активности (например, сафари): ")
guide_language = input("Язык гида (например, испанский): ")

user_input = {
    'Откуда': from_location,
    'Куда': to_location,
    'Бюджет': budget,
    'Тип тура': tour_type,
    'Цель тура': travel_purpose,
    'Трансфер': transfer,
    'Тип размещения': accommodation,
    'Питание': meal_plan,
    'Активности': activities,
    'Язык гида': guide_language
}

# Преобразование пользовательских данных
user_vector = pd.DataFrame(user_input, index=[0])
user_vector['Откуда'] = le.fit_transform(user_vector['Откуда'])
user_vector['Куда'] = le.fit_transform(user_vector['Куда'])
user_vector['Тип тура'] = le.fit_transform(user_vector['Тип тура'])
user_vector['Цель тура'] = le.fit_transform(user_vector['Цель тура'])
user_vector['Трансфер'] = le.fit_transform(user_vector['Трансфер'])
user_vector['Тип размещения'] = le.fit_transform(user_vector['Тип размещения'])
user_vector['Питание'] = le.fit_transform(user_vector['Питание'])
user_vector['Активности'] = le.fit_transform(user_vector['Активности'])
user_vector['Язык гида'] = le.fit_transform(user_vector['Язык гида'])

user_scaled = scaler.transform(user_vector)

# Вычисление косинусного сходства
similarity_scores = cosine_similarity(scaled_data, user_scaled)

# Получение индексов топ-5 наиболее похожих туров
top_5_indices = similarity_scores.flatten().argsort()[-5:][::-1]

# Вывод рекомендаций
print("\nТоп-5 рекомендуемых туров:")
for index in top_5_indices:
    recommended_tour = data.iloc[index]
    print(f"\nОткуда: {recommended_tour['Откуда']} - Куда: {recommended_tour['Куда']}")
    print(f"Бюджет: {recommended_tour['Бюджет']} руб")
    print(f"Тип тура: {recommended_tour['Тип тура']}, Цель тура: {recommended_tour['Цель тура']}")
    print(f"Трансфер: {recommended_tour['Трансфер']}, Тип размещения: {recommended_tour['Тип размещения']}")
    print(f"Питание: {recommended_tour['Питание']}, Активности: {recommended_tour['Активности']}")
    print(f"Язык гида: {recommended_tour['Язык гида']}")

