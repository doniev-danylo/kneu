# Крок 1: Генерація даних
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from pymongo import MongoClient

# Випадкове насіння для відтворюваності
np.random.seed(42)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['restaurant']
orders_count = list(db.orders_counter.find({}, {
    "_id": False,
    "X": True,
    "y": True,
    "date_range": True}))
print(orders_count)

# Генерація даних
n_samples = 101

X_new = np.linspace(0, 120, 121)

start_date = datetime(2023, 3, 1)
date_range = [start_date + timedelta(days=i) for i in range(122)]

# Створення DataFrame
data = pd.DataFrame(orders_count)
data['date_range'] = pd.to_datetime(data['date_range'], unit='ms')
print(data.to_json(orient='records'))
data_pred = pd.DataFrame({'X': X_new, 'date_range': date_range[:121]})

# Крок 2: Створення моделі лінійної регресії
from sklearn.linear_model import LinearRegression

# Створення та тренування моделі
model = LinearRegression()
model.fit(data[['X']], data['y'])

# Прогнозування
data_pred['y_pred'] = model.predict(data_pred[['X']])

# Крок 3: Візуалізація результатів
import plotly.express as px

# Створення графіка
fig = px.scatter(data, x='date_range', y='y')
fig.add_scatter(x=data_pred['date_range'], y=data_pred['y_pred'], mode='lines', name='Прогноз')
fig.update_layout(
    title='Прогнозування попиту за допомогою лінійної регресії',
    xaxis_title='Дні починаючи з березня 2023',
    yaxis_title='Попит'
)

# Крок 4: Збереження графіка в HTML-файл
fig.write_html("/Users/donevd/PycharmProjects/kneu/restaurant/templates/linear_regression_forecast.html")

# Виведення повідомлення про успішне збереження
print("Графік збережено у файл 'linear_regression_forecast.html'.")
