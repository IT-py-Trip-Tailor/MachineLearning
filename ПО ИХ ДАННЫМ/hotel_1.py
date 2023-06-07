def filter_hotels(hotels, min_stars=3, max_price=None, city=None):
    """
    Фильтрует список отелей по минимальному числу звезд, максимальной цене и городу.

    :param hotels: Список отелей.
    :param min_stars: Минимальное число звезд, по умолчанию 3.
    :param max_price: Максимальная цена, по умолчанию нет.
    :param city: Город, по умолчанию нет.
    :return: Отфильтрованный список отелей.
    """
    result = []

    for hotel in hotels:
        if hotel.stars < min_stars:
            continue
        if max_price is not None and hotel.price > max_price:
            continue
        if city is not None and hotel.city != city:
            continue
        result.append(hotel)

    return result

def sort_hotels(hotels, by='stars'):
    """
    Сортирует список отелей по заданному параметру.

    :param hotels: Список отелей.
    :param by: Параметр для сортировки, по умолчанию 'stars'.
    :return: Отсортированный список отелей.
    """
    return sorted(hotels, key=lambda hotel: getattr(hotel, by), reverse=True)
