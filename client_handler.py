import json
import traceback
from datetime import datetime


def index_wrapper(rates: json) -> json:  # excess code here
    _id = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']

    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': rates,
            }


def convert_all_wrapper(rates: json, to_rate_key: str) -> json:
    _id = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']

    currency = rates[to_rate_key]
    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': {key: rates[key] / currency for key in rates.keys()}
            }


def convert_wrapper(rates: json, from_rate_key: str, to_rate_key: str) -> json:
    _id = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']

    return {'id': _id,
            'response': 200,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': {'from': from_rate_key, 'to': to_rate_key,
                      'value': rates[to_rate_key] / rates[from_rate_key]}
            }
