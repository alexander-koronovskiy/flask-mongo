import json

import requests
from pymongo import MongoClient, database


# db connection
def db_conn(col: str) -> database:
    client = MongoClient('mongodb://localhost:27017/')
    return client[col]


# read and operate by query
def cursor_rates():
    return db_conn('rates')['rates']


# rates recording from outside api to db
def update_rates(url: str, keyword: str) -> json:
    col = db_conn('rates')['rates']
    rates = requests.get(url).json()[keyword]
    col.insert_one(rates)


# del last rates recording
def del_rates():
    cursor_rates().delete_one({})


# make jsonful check for this
def emergency_rates_to_client():
    return requests.get('https://www.cbr-xml-daily.ru/latest.js').json()['rates']
