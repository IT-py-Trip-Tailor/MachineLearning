import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Генерация данных для отелей
hotels_data = []
for i in range(100):
    hotels_data.append({
        'hotel_id': i + 1,
        'hotel_name': fake.company(),
        'stars': np.random.choice([3, 4, 5]),
        'price': np.random.randint(2000, 10000),
        'city': fake.city(),
        'rating': np.random.uniform(3.0, 5.0)
    })

# Генерация данных для транспорта
transport_data = []
for i in range(100):
    transport_data.append({
        'transport_id': i + 1,
        'type': np.random.choice(['train', 'bus', 'plane']),
        'price': np.random.randint(500, 5000),
        'origin_city': fake.city(),
        'destination_city': fake.city(),
        'duration': np.random.randint(1, 24)
    })

# Генерация данных для развлечений и экскурсий
activities_data = []
for i in range(100):
    activities_data.append({
        'activity_id': i + 1,
        'activity_name': fake.bs(),
        'price': np.random.randint(500, 3000),
        'city': fake.city(),
        'duration': np.random.randint(1, 8)
    })

# Создание DataFrame и сохранение в CSV-файлы
hotels_df = pd.DataFrame(hotels_data)
hotels_df.to_csv('hotels.csv', index=False)

transport_df = pd.DataFrame(transport_data)
transport_df.to_csv('transport.csv', index=False)

activities_df = pd.DataFrame(activities_data)
activities_df.to_csv('activities.csv', index=False)

# Генерация данных для туров
tour_data = []
interests_list = ['history', 'nature', 'culture', 'adventure', 'relaxation']

for i in range(100):
    hotel = np.random.choice(hotels_data)
    transport = np.random.choice(transport_data)
    activity = np.random.choice(activities_data)

    tour_data.append({
        'tour_id': i + 1,
        'hotel_id': hotel['hotel_id'],
        'transport_id': transport['transport_id'],
        'activity_id': activity['activity_id'],
        'interests': np.random.choice(interests_list),
        'budget': np.random.randint(5000, 30000),
        'duration': np.random.randint(1, 14),
        'accommodation_type': np.random.choice(['hostel', 'hotel', 'apartment']),
        'rating': np.random.uniform(3.0, 5.0)
    })

# Создание DataFrame и сохранение в CSV-файл
tours_df = pd.DataFrame(tour_data)
tours_df.to_csv('tours.csv', index=False)



