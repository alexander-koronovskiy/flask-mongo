import json


def json_handler(rates: json) -> json:
    rates['id'] = str(rates['_id'])  # is that correct serialization (?)
    rates['RUB'] = 1
    del rates['_id']
    return rates


def error_handler():
    pass
