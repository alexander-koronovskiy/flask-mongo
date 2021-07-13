import json

import requests
from pymongo import MongoClient


# получение курса валют по url стороннего api
def get_outside_rates(url: str, keyword: str) -> json:
    return requests.get(url).json()[keyword]


# создание
client = MongoClient("mongodb://localhost:27017/")
db = client["organisation"]


# запись тестовых данных в бд
col = db["developers"]
developer = {"name": "Lini", "address": "Sweden"}
col.insert_one(developer)
for row in client.list_databases():
    print(row)

# вывод из бд по наименованию валюты
# перезапись бд при перезагрузки приложения
