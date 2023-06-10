from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
    # Загрузка данных
    data = pd.read_csv('tour_data.csv')

    # Предобработка данных
    le = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == type(object):
            data[column] = le.fit_transform(data[column])

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Получение данных пользователя из POST-запроса
    user_input = request.get_json()

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

    return jsonify(recommended_tours.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
