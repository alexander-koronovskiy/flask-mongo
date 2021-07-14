import json

import requests
from pymongo import MongoClient, database


def get_outside_rates_old(url: str) -> json:
    return requests.get(url).json()


# db connection
def db_conn(col: str) -> database:
    client = MongoClient('mongodb://localhost:27017/')
    return client[col]


# rates recording from outside api to db
def record_outside_rates(url: str, keyword: str):
    col = db_conn('rates')['rates']
    rates = requests.get(url).json()[keyword]
    col.insert_one(rates)
    return rates
