from bson import ObjectId, json_util
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:password@localhost:27000/')
db = client['restaurant']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/menu', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        new_dish = request.json
        db.menu.insert_one(new_dish)
        return json_util.dumps(new_dish), 201
    if request.method == 'GET':
        menu = list(db.menu.find({}, {"_id": {"$toString": "$_id"},
                                      "name": True,
                                      "price": True}))
        return jsonify(menu)


@app.route('/menu/<dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    result = db.menu.delete_one({'_id': ObjectId(dish_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Dish deleted successfully'}), 200
    else:
        return jsonify({'error': 'Dish not found'}), 404


@app.route('/menu/change_name', methods=['POST'])
def change_name():
    if not (dish_id := request.json.get('_id')):
        return jsonify({'error': 'Missing dish ID'}), 400
    if not (new_name := request.json.get('name')):
        return jsonify({'error': 'Missing  name'}), 400

    result = db.menu.update_one({'_id': ObjectId(dish_id)}, {'$set': {'name': new_name}})
    if result.modified_count == 1:
        return jsonify({'message': 'Dish name updated successfully'}), 200
    else:
        return jsonify({'error': 'Dish not found'}), 404


@app.route('/menu/change_price', methods=['POST'])
def change_price():
    if not (dish_id := request.json.get('_id')):
        return jsonify({'error': 'Missing dish ID'}), 400
    if not (new_price := request.json.get('price')):
        return jsonify({'error': 'Missing  price'}), 400

    result = db.menu.update_one({'_id': ObjectId(dish_id)}, {'$set': {'price': new_price}})
    if result.modified_count == 1:
        return jsonify({'message': 'Dish price updated successfully'}), 200
    else:
        return jsonify({'error': 'Dish not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
