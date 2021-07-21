import json
from datetime import datetime


def wrap_schema(value: dict, id: str) -> dict:
    return {'id': id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': value,
            }


def index_wrapper(rates: json) -> json:
    """json response formation for index method"""
    _id = str(rates.pop('_id'))
    return wrap_schema(rates, _id)


def convert_all_wrapper(rates: json, to_rate_key: str) -> json:
    """json response formation for convert all method"""
    _id = str(rates.pop('_id'))
    currency = rates[to_rate_key]
    value = {key: rates[key] / currency for key in rates.keys()}
    return wrap_schema(value, _id)


def convert_wrapper(rates: json, from_rate_key: str, to_rate_key: str) -> json:
    """json response formation for convert method"""
    value = {'rates': {'from': from_rate_key, 'to': to_rate_key,
             'value': rates[to_rate_key] / rates[from_rate_key]},
             'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    return value
