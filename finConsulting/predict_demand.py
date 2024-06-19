# Крок 1: Генерація даних
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from pymongo import MongoClient

# Випадкове насіння для відтворюваності
np.random.seed(42)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['financialConsultingDB']

clients_count = list(db.clients_counter.find({}, {
    "_id": False,
    "X": True,
    "y": True,
    "date_range": True}))
print(clients_count)

# Генерація даних
n_samples = 101

X_new = np.linspace(0, 120, 121)

start_date = datetime(2024, 1, 1)
date_range = [start_date + timedelta(days=i) for i in range(122)]

# Створення DataFrame
data = pd.DataFrame(clients_count)
data['date_range'] = pd.to_datetime(data['date_range'], unit='ms')
print(data.to_json(orient='records'))

n_samples = 101
X = np.arange(n_samples)
y = np.exp(0.05 * X + np.random.normal(0, 0.2, n_samples))  # логарифмічне зростання з шумом
y = y.astype(int)  # приведення до цілочисельного типу

data = pd.DataFrame({'date_range': date_range[:101], 'X': X, 'y': y})

data_pred = pd.DataFrame({'X': X_new, 'date_range': date_range[:121]})

# Крок 2: Створення моделі лінійної регресії
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Створення та тренування моделі
degree = 2
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(data[['X']], data['y'])

# Прогнозування
data_pred['y_pred'] = model.predict(data_pred[['X']])

# Крок 3: Візуалізація результатів
import plotly.express as px

# Створення графіка
fig = px.scatter(data, x='date_range', y='y')
fig.add_scatter(x=data_pred['date_range'], y=data_pred['y_pred'], mode='lines', name='prediced amount')
fig.update_layout(
    title='revenue prediction',
    xaxis_title='day',
    yaxis_title='revenue',
    plot_bgcolor='rgba(240, 240, 1, 0.9)',  # фон графіка
    paper_bgcolor='rgba(240, 240, 240, 0.9)',  # фон паперу
    font=dict(family='Arial', size=14),  # шрифт
    width=1000, height=600  # розміри графіка
)

# Крок 4: Збереження графіка в HTML-файл
fig.write_html("/Users/donevd/PycharmProjects/kneu/finConsulting/templates/linear_regression_forecast.html")

# Виведення повідомлення про успішне збереження
print("Графік збережено у файл 'linear_regression_forecast.html'.")
