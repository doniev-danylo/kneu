from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:password@localhost:27000/')
mongo = client['financialConsultingDB']


@app.route('/')
def index():
    clients = list(mongo.clients.find())
    transactions = list(mongo.transactions.find())
    consultations = list(mongo.consultations.find())
    reports = list(mongo.reports.find())
    return render_template('index.html', clients=clients, transactions=transactions, consultations=consultations,
                           reports=reports)


@app.route('/linear_regression_forecast')
def linear_regression_forecast():
    return render_template('linear_regression_forecast.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
