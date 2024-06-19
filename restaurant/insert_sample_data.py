from datetime import datetime

from bson import ObjectId
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['financialConsultingDB']

menu_collection = db['clients_counter']

# Зразкові дані для додавання
sample_data = [{"X":0.0,"y":4.9671415301,"date_range":1677628800000},{"X":1.0,"y":1.1173569883,"date_range":1677715200000},{"X":2.0,"y":11.476885381,"date_range":1677801600000},{"X":3.0,"y":22.7302985641,"date_range":1677888000000},{"X":4.0,"y":7.6584662528,"date_range":1677974400000},{"X":5.0,"y":10.1586304305,"date_range":1678060800000},{"X":6.0,"y":30.7921281551,"date_range":1678147200000},{"X":7.0,"y":25.1743472915,"date_range":1678233600000},{"X":8.0,"y":15.3052561407,"date_range":1678320000000},{"X":9.0,"y":27.9256004359,"date_range":1678406400000},{"X":10.0,"y":20.3658230719,"date_range":1678492800000},{"X":11.0,"y":22.8427024643,"date_range":1678579200000},{"X":12.0,"y":32.4196227157,"date_range":1678665600000},{"X":13.0,"y":13.3671975534,"date_range":1678752000000},{"X":14.0,"y":17.7508216749,"date_range":1678838400000},{"X":15.0,"y":31.8771247076,"date_range":1678924800000},{"X":16.0,"y":29.8716887967,"date_range":1679011200000},{"X":17.0,"y":45.642473326,"date_range":1679097600000},{"X":18.0,"y":35.9197592448,"date_range":1679184000000},{"X":19.0,"y":33.3769629866,"date_range":1679270400000},{"X":20.0,"y":64.6564876892,"date_range":1679356800000},{"X":21.0,"y":50.2422369951,"date_range":1679443200000},{"X":22.0,"y":55.6752820469,"date_range":1679529600000},{"X":23.0,"y":43.2525181379,"date_range":1679616000000},{"X":24.0,"y":54.5561727547,"date_range":1679702400000},{"X":25.0,"y":63.6092258971,"date_range":1679788800000},{"X":26.0,"y":53.4900642258,"date_range":1679875200000},{"X":27.0,"y":71.2569801835,"date_range":1679961600000},{"X":28.0,"y":63.9936131008,"date_range":1680048000000},{"X":29.0,"y":69.5830625021,"date_range":1680134400000},{"X":30.0,"y":68.9829338777,"date_range":1680220800000},{"X":31.0,"y":96.0227818451,"date_range":1680307200000},{"X":32.0,"y":79.8650277526,"date_range":1680393600000},{"X":33.0,"y":71.9228907104,"date_range":1680480000000},{"X":34.0,"y":93.225449121,"date_range":1680566400000},{"X":35.0,"y":75.2915635003,"date_range":1680652800000},{"X":36.0,"y":92.08863595,"date_range":1680739200000},{"X":37.0,"y":72.9032987612,"date_range":1680825600000},{"X":38.0,"y":81.718139511,"date_range":1680912000000},{"X":39.0,"y":99.4686123587,"date_range":1680998400000},{"X":40.0,"y":107.3846658,"date_range":1681084800000},{"X":41.0,"y":104.2136828119,"date_range":1681171200000},{"X":42.0,"y":103.8435171761,"date_range":1681257600000},{"X":43.0,"y":104.4889630441,"date_range":1681344000000},{"X":44.0,"y":95.2147800963,"date_range":1681430400000},{"X":45.0,"y":105.3015579161,"date_range":1681516800000},{"X":46.0,"y":110.3936122904,"date_range":1681603200000},{"X":47.0,"y":128.0712222622,"date_range":1681689600000},{"X":48.0,"y":123.4361828957,"date_range":1681776000000},{"X":49.0,"y":104.8695984464,"date_range":1681862400000},{"X":50.0,"y":128.2408396939,"date_range":1681948800000},{"X":51.0,"y":123.6491771958,"date_range":1682035200000},{"X":52.0,"y":123.2307799969,"date_range":1682121600000},{"X":53.0,"y":138.6167628884,"date_range":1682208000000},{"X":54.0,"y":145.309995225,"date_range":1682294400000},{"X":55.0,"y":146.8128011912,"date_range":1682380800000},{"X":56.0,"y":131.6078247678,"date_range":1682467200000},{"X":57.0,"y":139.4078762415,"date_range":1682553600000},{"X":58.0,"y":148.312634314,"date_range":1682640000000},{"X":59.0,"y":157.2554512712,"date_range":1682726400000},{"X":60.0,"y":145.2082576215,"date_range":1682812800000},{"X":61.0,"y":150.6434102334,"date_range":1682899200000},{"X":62.0,"y":143.9366502599,"date_range":1682985600000},{"X":63.0,"y":145.5379337592,"date_range":1683072000000},{"X":64.0,"y":168.1252582239,"date_range":1683158400000},{"X":65.0,"y":176.0624002857,"date_range":1683244800000},{"X":66.0,"y":164.2798987842,"date_range":1683331200000},{"X":67.0,"y":177.5353289789,"date_range":1683417600000},{"X":68.0,"y":173.6163602505,"date_range":1683504000000},{"X":69.0,"y":166.0488024539,"date_range":1683590400000},{"X":70.0,"y":178.6139560551,"date_range":1683676800000},{"X":71.0,"y":192.8803656647,"date_range":1683763200000},{"X":72.0,"y":179.6417396089,"date_range":1683849600000},{"X":73.0,"y":198.1464365581,"date_range":1683936000000},{"X":74.0,"y":158.8025489591,"date_range":1684022400000},{"X":75.0,"y":195.7190250438,"date_range":1684108800000},{"X":76.0,"y":190.8704706824,"date_range":1684195200000},{"X":77.0,"y":189.5099264953,"date_range":1684281600000},{"X":78.0,"y":195.9176077654,"date_range":1684368000000},{"X":79.0,"y":177.624310854,"date_range":1684454400000},{"X":80.0,"y":197.8032811216,"date_range":1684540800000},{"X":81.0,"y":206.0711257151,"date_range":1684627200000},{"X":82.0,"y":219.7789404474,"date_range":1684713600000},{"X":83.0,"y":202.3172978173,"date_range":1684800000000},{"X":84.0,"y":201.9150639711,"date_range":1684886400000},{"X":85.0,"y":207.4824295642,"date_range":1684972800000},{"X":86.0,"y":224.154021177,"date_range":1685059200000},{"X":87.0,"y":220.7875110966,"date_range":1685145600000},{"X":88.0,"y":214.7023979623,"date_range":1685232000000},{"X":89.0,"y":227.6326743311,"date_range":1685318400000},{"X":90.0,"y":225.9707754935,"date_range":1685404800000},{"X":91.0,"y":237.1864499053,"date_range":1685491200000},{"X":92.0,"y":222.9794690612,"date_range":1685577600000},{"X":93.0,"y":229.223378534,"date_range":1685664000000},{"X":94.0,"y":231.0789184687,"date_range":1685750400000},{"X":95.0,"y":222.8648505187,"date_range":1685836800000},{"X":96.0,"y":242.9612027706,"date_range":1685923200000},{"X":97.0,"y":245.1105527218,"date_range":1686009600000},{"X":98.0,"y":245.0511345664,"date_range":1686096000000},{"X":99.0,"y":245.1541286662,"date_range":1686182400000},{"X":100.0,"y":235.8462925795,"date_range":1686268800000}]



# Додавання зразкових даних до колекції
menu_collection.insert_many(sample_data)
#
# db = client['restaurant']
#
# menu_collection = db['orders']
#
# # Зразкові дані для додавання
# sample_data = [
#
#     {
#         "_id": ObjectId("665b23057ee0abf056f20a50"),
#         "customer": "Bob Williams",
#         "timestamp_order": datetime(2024, 5, 15, 13, 45, 23),
#         "timestamp_pay": datetime(2024, 5, 15, 14, 15, 23),
#         "total_price": 18.0,
#         "items": [
#             {"_id": ObjectId("665b22057ee0abf056f20a46"), "name": "Caesar Salad", "price": 7.5, "quantity": 1},
#             {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1},
#             {"_id": ObjectId("665b22057ee0abf056f20a47"), "name": "Tiramisu", "price": 6.0, "quantity": 1}
#         ],
#         "waiter_tips": 3.0,
#         "payment_method": "Cash",
#         "waiter": {"id": "w002", "name": "Sarah Brown"}
#     },
#     {
#         "_id": ObjectId("665b23057ee0abf056f20a51"),
#         "customer": "Charlie Davis",
#         "timestamp_order": datetime(2024, 5, 15, 14, 23, 12),
#         "timestamp_pay": datetime(2024, 5, 15, 15, 3, 12),
#         "total_price": 12.5,
#         "items": [
#             {"_id": ObjectId("665b22057ee0abf056f20a44"), "name": "Spaghetti", "price": 12.5, "quantity": 1}
#         ],
#         "waiter_tips": 2.0,
#         "payment_method": "Debit Card",
#         "waiter": {"id": "w003", "name": "Emily White"}
#     },
#     {
#         "_id": ObjectId("665b23057ee0abf056f20a52"),
#         "customer": "David Miller",
#         "timestamp_order": datetime(2024, 5, 15, 15, 56, 32),
#         "timestamp_pay": datetime(2024, 5, 15, 16, 31, 32),
#         "total_price": 21.0,
#         "items": [
#             {"_id": ObjectId("665b22057ee0abf056f20a45"), "name": "Margherita Pizza", "price": 8.0, "quantity": 1},
#             {"_id": ObjectId("665b22057ee0abf056f20a46"), "name": "Caesar Salad", "price": 7.5, "quantity": 1},
#             {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1}
#         ],
#         "waiter_tips": 3.5,
#         "payment_method": "Credit Card",
#         "waiter": {"id": "w004", "name": "Michael Green"}
#     },
#     {
#         "_id": ObjectId("665b23057ee0abf056f20a53"),
#         "customer": "Emma Wilson",
#         "timestamp_order": datetime(2024, 5, 15, 16, 34, 56),
#         "timestamp_pay": datetime(2024, 5, 15, 17, 9, 56),
#         "total_price": 17.5,
#         "items": [
#             {"_id": ObjectId("665b22057ee0abf056f20a47"), "name": "Tiramisu", "price": 6.0, "quantity": 2},
#             {"_id": ObjectId("665b22057ee0abf056f20a48"), "name": "Minestrone Soup", "price": 5.5, "quantity": 1}
#         ],
#         "waiter_tips": 2.5,
#         "payment_method": "Credit Card",
#         "waiter": {"id": "w005", "name": "Laura Blue"}
#     }
#
# ]
# menu_collection.insert_many(sample_data)
#
# db = client['restaurant']
#
# # Колекція з бронюваннями
# reservations_collection = db['reservations']
#
# # Тестові дані для бронювань
# reservations = [
#     {
#         "_id": ObjectId(),
#         "customer": "Alice Johnson",
#         "timestamp_reservation": datetime(2024, 6, 1, 10, 0, 0),
#         "timestamp_visit": datetime(2024, 6, 1, 19, 0, 0),
#         "table_number": 5,
#         "number_of_guests": 2,
#         "special_requests": "Window seat",
#         "contact_phone": "+1234567890",
#         "is_confirmed": True,
#         "waiter": {"id": "w001", "name": "John Smith"}
#     },
#     {
#         "_id": ObjectId(),
#         "customer": "Bob Williams",
#         "timestamp_reservation": datetime(2024, 6, 2, 12, 30, 0),
#         "timestamp_visit": datetime(2024, 6, 2, 20, 0, 0),
#         "table_number": 3,
#         "number_of_guests": 4,
#         "special_requests": "High chair for baby",
#         "contact_phone": "+0987654321",
#         "is_confirmed": True,
#         "waiter": {"id": "w002", "name": "Sarah Brown"}
#     },
#     {
#         "_id": ObjectId(),
#         "customer": "Charlie Davis",
#         "timestamp_reservation": datetime(2024, 6, 3, 14, 0, 0),
#         "timestamp_visit": datetime(2024, 6, 3, 18, 30, 0),
#         "table_number": 7,
#         "number_of_guests": 3,
#         "special_requests": "Birthday cake",
#         "contact_phone": "+1122334455",
#         "is_confirmed": False,
#         "waiter": {"id": "w003", "name": "Emily White"}
#     },
#     {
#         "_id": ObjectId(),
#         "customer": "David Miller",
#         "timestamp_reservation": datetime(2024, 6, 4, 16, 45, 0),
#         "timestamp_visit": datetime(2024, 6, 4, 19, 45, 0),
#         "table_number": 1,
#         "number_of_guests": 5,
#         "special_requests": "Quiet area",
#         "contact_phone": "+1223344556",
#         "is_confirmed": True,
#         "waiter": {"id": "w004", "name": "Michael Green"}
#     },
#     {
#         "_id": ObjectId(),
#         "customer": "Emma Wilson",
#         "timestamp_reservation": datetime(2024, 6, 5, 11, 15, 0),
#         "timestamp_visit": datetime(2024, 6, 5, 21, 0, 0),
#         "table_number": 8,
#         "number_of_guests": 6,
#         "special_requests": "Vegetarian menu",
#         "contact_phone": "+1445566778",
#         "is_confirmed": True,
#         "waiter": {"id": "w005", "name": "Laura Blue"}
#     }
# ]
#
# # Вставка тестових даних у колекцію бронювань
# reservations_collection.insert_many(reservations)
#
# waiters_collection = db['waiters']
#
# # Тестові дані для офіціантів
# waiters = [
#     {
#         "_id": ObjectId(),
#         "name": "John Smith",
#         "age": 28,
#         "gender": "Male",
#         "shift": "Morning",
#         "experience": 4,
#         "rating": 4.5
#     },
#     {
#         "_id": ObjectId(),
#         "name": "Sarah Brown",
#         "age": 24,
#         "gender": "Female",
#         "shift": "Evening",
#         "experience": 2,
#         "rating": 4.0
#     },
#     {
#         "_id": ObjectId(),
#         "name": "Emily White",
#         "age": 30,
#         "gender": "Female",
#         "shift": "Morning",
#         "experience": 6,
#         "rating": 4.8
#     },
#     {
#         "_id": ObjectId(),
#         "name": "Michael Green",
#         "age": 35,
#         "gender": "Male",
#         "shift": "Evening",
#         "experience": 8,
#         "rating": 4.9
#     },
#     {
#         "_id": ObjectId(),
#         "name": "Laura Blue",
#         "age": 26,
#         "gender": "Female",
#         "shift": "Morning",
#         "experience": 3,
#         "rating": 4.2
#     }
# ]
#
# # Вставка тестових даних у колекцію офіціантів
# waiters_collection.insert_many(waiters)
