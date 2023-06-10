import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Загружаем предпочтения пользователя и данные об услугах
user_prefs = pd.read_csv("user_prefs.csv")
services = pd.read_csv("services.csv")

# Масштабируем данные
scaler = MinMaxScaler()
user_prefs_scaled = scaler.fit_transform(user_prefs)
services_scaled = scaler.transform(services)

# Вычисляем сходство и получаем топ-5 услуг
similarity_matrix = cosine_similarity(user_prefs_scaled, services_scaled)
top_service_indices = similarity_matrix[0].argsort()[-5:][::-1]
top_services = services.iloc[top_service_indices]

user_feedback = get_user_feedback(top_services)

# Обновляем предпочтения пользователя на основе обратной связи
# Обратная связь - это рейтинг каждой услуги от 1 до 5
for i, service_index in enumerate(top_service_indices):
    user_prefs.loc[service_index] = (user_prefs.loc[service_index] + user_feedback[i]) / 2

# Сохраняем обновленные предпочтения пользователя для использования в будущих рекомендациях
user_prefs.to_csv("user_prefs.csv", index=False)
