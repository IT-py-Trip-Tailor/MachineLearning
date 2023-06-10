import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout, Embedding, MultiHeadAttention, LayerNormalization
from tensorflow.keras.models import Model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Данные
user_behavior_data = [...]  #  данные о поведении пользователя
product_data = [...]  #  данные о продуктах и услугах
user_preferences_data = [...]  # данные о предпочтениях пользователя


# Модель трансформера
class Transformer(tf.keras.Model):
    def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size, maximum_position_encoding, rate=0.1):
        super(Transformer, self).__init__()

        self.embedding = Embedding(input_vocab_size, d_model)
        self.pos_encoding = positional_encoding(maximum_position_encoding, d_model)

        self.transformer_layers = [TransformerLayer(d_model, num_heads, dff, rate) for _ in range(num_layers)]
        self.dropout = Dropout(rate)

    def call(self, x, training, mask):
        seq_len = tf.shape(x)[1]

        x = self.embedding(x)
        x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
        x += self.pos_encoding[:, :seq_len, :]

        x = self.dropout(x, training=training)

        for i in range(self.num_layers):
            x = self.transformer_layers[i](x, training, mask)

        return x


transformer_model = Transformer(...)
transformer_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
transformer_model.fit(user_behavior_data, epochs=10)

# Модель фильтрации на основе содержания
vectorizer = TfidfVectorizer()
product_matrix = vectorizer.fit_transform(product_data)


def recommend_products(user_preferences):
    user_vector = vectorizer.transform([user_preferences])
    similarity_scores = cosine_similarity(user_vector, product_matrix)
    recommended_products = similarity_scores.argsort()[0][-10:]
    return recommended_products


# Пример использования модели для рекомендации продуктов
user_preferences = user_preferences_data[0]
recommended_products = recommend_products(user_preferences)
print(recommended_products)
