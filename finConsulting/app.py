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


if __name__ == '__main__':
    app.run(debug=True)
