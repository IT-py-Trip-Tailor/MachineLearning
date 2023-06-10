from flask import Flask, request, render_template
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

# KNN алгоритм
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(scaled_data)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = {
            'Откуда': request.form.get('from'),
            'Куда': request.form.get('where'),
            'Бюджет': request.form.get('budget'),
            'Тип тура': request.form.get('type_tour'),
            'Цель тура': request.form.get('target'),
            'Трансфер': request.form.get('transfer'),
            'Тип размещения': request.form.get('accommodation_type'),
            'Питание': request.form.get('meal'),
            'Активности': request.form.get('activities'),
            'Язык гида': request.form.get('guide_language')
        }

        # Преобразование пользовательских данных
        for col, value in user_input.items():
            if col in le.classes_:
                user_input[col] = le.transform([value])[0]

        user_data = scaler.transform(pd.DataFrame([user_input]))

        _, indices = knn.kneighbors(user_data)

        # Вывод результатов
        recommended_tours = data.iloc[indices[0]]

        return render_template('results.html', recommendations=recommended_tours)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
