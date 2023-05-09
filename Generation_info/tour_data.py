import random
import csv
from datetime import datetime, timedelta

# Генерация случайных данных
def generate_random_data(num_samples):
    locations = ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Екатеринбург', 'Новосибирск', 'Калининград', 'Владивосток', 'Мурманск', 'Самара']
    tour_types = ['отдых', 'экскурсии', 'приключения', 'культурный', 'спорт', 'гастрономический', 'здоровье', 'обучение', 'экотуризм']
    travel_purposes = ['отпуск', 'деловая поездка', 'развлечения', 'посещение родственников', 'учеба', 'конференции', 'лечение']
    accommodation_types = ['отель', 'апартаменты', 'хостел', 'гостевой дом', 'коттедж', 'бунгало', 'кемпинг']
    meal_plans = ['без питания', 'завтрак', 'полупансион', 'полный пансион', 'все включено']
    activities = ['пляж', 'горные лыжи', 'пешие прогулки', 'велосипедные прогулки', 'посещение музеев', 'посещение исторических мест', 'посещение тематических парков', 'водные виды спорта', 'сафари']
    group_size = [1, 2, 3, 4, 5, 6]
    ages = [18, 25, 35, 45, 55, 65, 75]
    guide_language = ['русский', 'английский', 'немецкий', 'французский', 'испанский', 'итальянский', 'китайский']

    data = []

    for _ in range(num_samples):
        start_location = random.choice(locations)
        end_location = random.choice([loc for loc in locations if loc != start_location])
        start_date = datetime.now() + timedelta(days=random.randint(1, 365))
        end_date = start_date + timedelta(days=random.randint(1, 21))
        budget = random.randint(5000, 200000)
        tour_type = random.choice(tour_types)
        route = f"{start_location} - {end_location}"
        travel_purpose = random.choice(travel_purposes)
        transfer = random.choice(['автобус', 'поезд', 'самолет'])
        accommodation = random.choice(accommodation_types)
        meal_plan = random.choice(meal_plans)
        activity = random.choice(activities)
        hotel_stars = random.randint(1, 5)
        group = random.choice(group_size)
        age = random.choice(ages)
        language = random.choice(guide_language)

        data.append({
            'Откуда': start_location,
            'Куда': end_location,
            'Даты': f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}",
            'Бюджет': budget,
            'Тип тура': tour_type,
            'Маршрут': route,
            'Цель тура': travel_purpose,
            'Трансфер': transfer,
            'Тип размещения': accommodation,
            'Питание': meal_plan,
            'Активности': activity,
            'Звезды отеля': hotel_stars,
            'Размер группы': group,
            'Возраст': age,
            'Язык гида': language
        })
    return data

# Генерируем случайные данные (например, 10000 записей)
random_data = generate_random_data(1000000)

# Сохраняем данные в CSV-файл
with open('tour_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Откуда', 'Куда', 'Даты', 'Бюджет', 'Тип тура', 'Маршрут', 'Цель тура', 'Трансфер',
                  'Тип размещения', 'Питание', 'Активности', 'Звезды отеля', 'Размер группы', 'Возраст', 'Язык гида']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in random_data:
        writer.writerow(item)
# Сохранение данных в файл CSV
tour_data.to_csv('tour_data.csv', index=False)



