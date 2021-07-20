import json
from datetime import datetime

# release schema, pop methods for id,
# add test rub cases in test index, cl handler tests

def index_wrapper(rates: json) -> json:
    """json response formation for index method"""
    _id = str(rates['_id'])
    del rates['_id']
    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': rates,
            }


def convert_all_wrapper(rates: json, to_rate_key: str) -> json:
    """json response formation for convert all method"""
    _id = str(rates['_id'])
    del rates['_id']
    currency = rates[to_rate_key]
    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': {key: rates[key] / currency for key in rates.keys()}
            }


def convert_wrapper(rates: json, from_rate_key: str, to_rate_key: str) -> json:
    """json response formation for convert method"""
    _id = str(rates['_id'])
    del rates['_id']
    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': {'from': from_rate_key, 'to': to_rate_key,
                      'value': rates[to_rate_key] / rates[from_rate_key]}
            }
