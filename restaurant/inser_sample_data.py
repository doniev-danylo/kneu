from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['restaurant']

menu_collection = db['menu']

# Зразкові дані для додавання
sample_data = [
    {"name": "Spaghetti Carbonara", "price": 12.5},
    {"name": "Margherita Pizza", "price": 8.0},
    {"name": "Caesar Salad", "price": 7.5},
    {"name": "Tiramisu", "price": 6.0},
    {"name": "Minestrone Soup", "price": 5.5}
]

# Додавання зразкових даних до колекції
menu_collection.insert_many(sample_data)