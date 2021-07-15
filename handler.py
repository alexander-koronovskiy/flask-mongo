import json

import requests
from pymongo import MongoClient, cursor, database


def db_conn(col: str) -> database:
    """db connection"""
    client = MongoClient('mongodb://localhost:27017/')
    return client[col]


def cursor_rates() -> cursor:
    """read and operate by query"""
    return db_conn('rates')['rates']


def update_rates(url: str, keyword: str) -> json:
    """rates recording from outside api to db"""
    rates = requests.get(url).json()[keyword]
    cursor_rates().insert_one(rates)


def del_rates() -> None:
    """del last rates recording"""
    cursor_rates().delete_one({})


# make jsonful check for this
def emergency_rates_to_client() -> json:
    return requests.get('https://www.cbr-xml-daily.ru/latest.js').json()['rates']
