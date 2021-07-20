import json
import traceback
from datetime import datetime


# index wrapper
def json_handler(rates: json) -> json:
    _id = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']
    return {'id': _id,
            'response': 200,
            'rates': rates,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            }


def convert_wrapper():
    pass


def convert_all_wrapper():
    pass
