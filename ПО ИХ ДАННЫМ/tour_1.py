def filter_tours(tours, budget, preferred_city, duration, tour_type):
    """
    Фильтрация списка туров по заданным критериям.
    """
    filtered_tours = [tour for tour in tours if tour.price <= budget and
                      tour.city == preferred_city and
                      tour.days == duration and
                      tour.tour_type == tour_type]
    return filtered_tours


def rank_tours(tours):
    """
    Ранжирование отфильтрованного списка туров.
    Здесь мы предполагаем, что туры ранжируются по количеству звезд отеля,
    но вы можете использовать любые другие критерии.
    """
    ranked_tours = sorted(tours, key=lambda x: x.hotel_stars, reverse=True)
    return ranked_tours


def get_optimal_tour(tours, user_input):
    """
    Выбор оптимального тура из списка туров на основе пользовательского ввода.
    """
    budget = user_input['budget']
    preferred_city = user_input['city']
    duration = user_input['days']
    tour_type = user_input['tour_type']

    # Фильтрация туров
    filtered_tours = filter_tours(tours, budget, preferred_city, duration, tour_type)

    # Ранжирование отфильтрованных туров
    ranked_tours = rank_tours(filtered_tours)

    # Возврат самого высоко ранжированного тура
    if ranked_tours:
        return ranked_tours[0]
    else:
        return None
