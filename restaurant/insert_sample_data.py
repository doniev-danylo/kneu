from datetime import datetime

from bson import ObjectId
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['restaurant']

menu_collection = db['orders']

# Зразкові дані для додавання
sample_data = [
    {"items": "Spaghetti Carbonara", "price": 12.5},
    {"name": "Margherita Pizza", "price": 8.0},
    {"name": "Caesar Salad", "price": 7.5},
    {"name": "Tiramisu", "price": 6.0},
    {"name": "Minestrone Soup", "price": 5.5}
]

# Додавання зразкових даних до колекції
menu_collection.insert_many(sample_data)

db = client['restaurant']

menu_collection = db['orders']

# Зразкові дані для додавання
sample_data = [

    {
        "_id": ObjectId("665b23057ee0abf056f20a50"),
        "customer": "Bob Williams",
        "timestamp_order": datetime(2024, 5, 15, 13, 45, 23),
        "timestamp_pay": datetime(2024, 5, 15, 14, 15, 23),
        "total_price": 18.0,
        "items": [
            {"_id": ObjectId("665b22057ee0abf056f20a46"), "name": "Caesar Salad", "price": 7.5, "quantity": 1},
            {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1},
            {"_id": ObjectId("665b22057ee0abf056f20a47"), "name": "Tiramisu", "price": 6.0, "quantity": 1}
        ],
        "waiter_tips": 3.0,
        "payment_method": "Cash",
        "waiter": {"id": "w002", "name": "Sarah Brown"}
    },
    {
        "_id": ObjectId("665b23057ee0abf056f20a51"),
        "customer": "Charlie Davis",
        "timestamp_order": datetime(2024, 5, 15, 14, 23, 12),
        "timestamp_pay": datetime(2024, 5, 15, 15, 3, 12),
        "total_price": 12.5,
        "items": [
            {"_id": ObjectId("665b22057ee0abf056f20a44"), "name": "Spaghetti", "price": 12.5, "quantity": 1}
        ],
        "waiter_tips": 2.0,
        "payment_method": "Debit Card",
        "waiter": {"id": "w003", "name": "Emily White"}
    },
    {
        "_id": ObjectId("665b23057ee0abf056f20a52"),
        "customer": "David Miller",
        "timestamp_order": datetime(2024, 5, 15, 15, 56, 32),
        "timestamp_pay": datetime(2024, 5, 15, 16, 31, 32),
        "total_price": 21.0,
        "items": [
            {"_id": ObjectId("665b22057ee0abf056f20a45"), "name": "Margherita Pizza", "price": 8.0, "quantity": 1},
            {"_id": ObjectId("665b22057ee0abf056f20a46"), "name": "Caesar Salad", "price": 7.5, "quantity": 1},
            {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1}
        ],
        "waiter_tips": 3.5,
        "payment_method": "Credit Card",
        "waiter": {"id": "w004", "name": "Michael Green"}
    },
    {
        "_id": ObjectId("665b23057ee0abf056f20a53"),
        "customer": "Emma Wilson",
        "timestamp_order": datetime(2024, 5, 15, 16, 34, 56),
        "timestamp_pay": datetime(2024, 5, 15, 17, 9, 56),
        "total_price": 17.5,
        "items": [
            {"_id": ObjectId("665b22057ee0abf056f20a47"), "name": "Tiramisu", "price": 6.0, "quantity": 2},
            {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1}
        ],
        "waiter_tips": 2.5,
        "payment_method": "Credit Card",
        "waiter": {"id": "w005", "name": "Laura Blue"}
    }

]
menu_collection.insert_many(sample_data)

db = client['restaurant']

# Колекція з бронюваннями
reservations_collection = db['reservations']

# Тестові дані для бронювань
reservations = [
    {
        "_id": ObjectId(),
        "customer": "Alice Johnson",
        "timestamp_reservation": datetime(2024, 6, 1, 10, 0, 0),
        "timestamp_visit": datetime(2024, 6, 1, 19, 0, 0),
        "table_number": 5,
        "number_of_guests": 2,
        "special_requests": "Window seat",
        "contact_phone": "+1234567890",
        "is_confirmed": True,
        "waiter": {"id": "w001", "name": "John Smith"}
    },
    {
        "_id": ObjectId(),
        "customer": "Bob Williams",
        "timestamp_reservation": datetime(2024, 6, 2, 12, 30, 0),
        "timestamp_visit": datetime(2024, 6, 2, 20, 0, 0),
        "table_number": 3,
        "number_of_guests": 4,
        "special_requests": "High chair for baby",
        "contact_phone": "+0987654321",
        "is_confirmed": True,
        "waiter": {"id": "w002", "name": "Sarah Brown"}
    },
    {
        "_id": ObjectId(),
        "customer": "Charlie Davis",
        "timestamp_reservation": datetime(2024, 6, 3, 14, 0, 0),
        "timestamp_visit": datetime(2024, 6, 3, 18, 30, 0),
        "table_number": 7,
        "number_of_guests": 3,
        "special_requests": "Birthday cake",
        "contact_phone": "+1122334455",
        "is_confirmed": False,
        "waiter": {"id": "w003", "name": "Emily White"}
    },
    {
        "_id": ObjectId(),
        "customer": "David Miller",
        "timestamp_reservation": datetime(2024, 6, 4, 16, 45, 0),
        "timestamp_visit": datetime(2024, 6, 4, 19, 45, 0),
        "table_number": 1,
        "number_of_guests": 5,
        "special_requests": "Quiet area",
        "contact_phone": "+1223344556",
        "is_confirmed": True,
        "waiter": {"id": "w004", "name": "Michael Green"}
    },
    {
        "_id": ObjectId(),
        "customer": "Emma Wilson",
        "timestamp_reservation": datetime(2024, 6, 5, 11, 15, 0),
        "timestamp_visit": datetime(2024, 6, 5, 21, 0, 0),
        "table_number": 8,
        "number_of_guests": 6,
        "special_requests": "Vegetarian menu",
        "contact_phone": "+1445566778",
        "is_confirmed": True,
        "waiter": {"id": "w005", "name": "Laura Blue"}
    }
]

# Вставка тестових даних у колекцію бронювань
reservations_collection.insert_many(reservations)

waiters_collection = db['waiters']

# Тестові дані для офіціантів
waiters = [
    {
        "_id": ObjectId(),
        "name": "John Smith",
        "age": 28,
        "gender": "Male",
        "shift": "Morning",
        "experience": 4,
        "rating": 4.5
    },
    {
        "_id": ObjectId(),
        "name": "Sarah Brown",
        "age": 24,
        "gender": "Female",
        "shift": "Evening",
        "experience": 2,
        "rating": 4.0
    },
    {
        "_id": ObjectId(),
        "name": "Emily White",
        "age": 30,
        "gender": "Female",
        "shift": "Morning",
        "experience": 6,
        "rating": 4.8
    },
    {
        "_id": ObjectId(),
        "name": "Michael Green",
        "age": 35,
        "gender": "Male",
        "shift": "Evening",
        "experience": 8,
        "rating": 4.9
    },
    {
        "_id": ObjectId(),
        "name": "Laura Blue",
        "age": 26,
        "gender": "Female",
        "shift": "Morning",
        "experience": 3,
        "rating": 4.2
    }
]

# Вставка тестових даних у колекцію офіціантів
waiters_collection.insert_many(waiters)
