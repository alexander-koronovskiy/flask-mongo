import json

import requests
from pymongo import MongoClient


# получение курса валют по url стороннего api
def get_outside_rates(url: str, keyword: str) -> json:
    return requests.get(url).json()[keyword]


def get_outside_rates_old(url: str) -> json:
    return requests.get(url).json()


# создание
client = MongoClient("mongodb://localhost:27017/")
db = client["rates"]

# запись тестовых данных в бд
col = db["rates"]
rates = get_outside_rates("https://www.cbr-xml-daily.ru/latest.js", "rates")
col.insert_one(rates)

# принт данных из бд
for row in db.rates.find():
    print(row)

# очистка бд при перезагрузки приложения
# db.rates.remove()
