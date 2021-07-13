import json

import requests
from pymongo import MongoClient, database


def get_outside_rates_old(url: str) -> json:
    return requests.get(url).json()


# подключение к бд
def db_conn(col: str) -> database:
    client = MongoClient("mongodb://localhost:27017/")
    return client[col]


# запись курса валют из стороннего api в бд
def record_outside_rates(url: str, keyword: str):
    col = db_conn("rates")["rates"]
    rates = requests.get(url).json()[keyword]
    col.insert_one(rates)
    return rates


# принт данных из бд
rates = record_outside_rates("https://www.cbr-xml-daily.ru/latest.js", "rates")
for row in db_conn("rates").rates.find():
    print(row)

# очистка бд при перезагрузки приложения
# db_conn("rates").rates.remove()
