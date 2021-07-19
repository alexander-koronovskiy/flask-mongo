import json


def json_handler(rates: json) -> json:
    rates['_id'] = str(rates['_id'])  # is that correct serialization (?)
    rates['RUB'] = 1
    return rates


def error_handler():
    pass
