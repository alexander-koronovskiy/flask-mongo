import json

import requests
from jsonschema import validate
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
    pass


# from api to client without db - emergency case


# expected json schema example
schema = {
    'type': 'object',
    'properties': {
        'description': {'type': 'string'},
        'status': {'type': 'boolean'},
        'value_a': {'type': 'number'},
        'value_b': {'type': 'number'},
    },
}

temp_data = '{"description": "Hello world!", "status": true, "value_a": 1, "value_b": 3.14}'


# try to validate and send to client temporary json
def post_json_to_client(row: json) -> json:
    my_json = json.loads(row)
    validate(instance=my_json, schema=schema)
    return my_json
