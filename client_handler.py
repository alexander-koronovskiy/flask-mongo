import json
from datetime import datetime

import flask


def wrap_success_schema(value: dict, id: str) -> dict:
    """json wrapper for success response"""
    return {'id': id,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'rates': value,
            }


def index_wrapper(rates: json) -> json:
    """json response formation from mongo"""
    _id = str(rates.pop('_id'))
    return wrap_success_schema(rates, _id)


def convert_all_wrapper(rates: json, to_rate_key: str) -> json:
    """json response formation for convert all method"""
    _id = str(rates.pop('_id'))
    currency = rates[to_rate_key]
    value = {key: rates[key] / currency for key in rates.keys()}
    return wrap_success_schema(value, _id)


def convert_wrapper(rates: json, from_: str, to_: str, value_: str) -> json:
    """json response formation for convert method"""
    rates = index_wrapper(rates)['rates']
    return {'ur cash': {from_: value_},
            'convert': {to_: value_ * rates[to_] / rates[from_]}}


def err_json_report(app: flask.app, resp_code: int):  # this method must returns Flask Response Object
    """json err log builder for bad get or post requests"""
    data = {'message': 'wrong rates convert parameters or app internal error',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    response = app.response_class(
        response=json.dumps(data),  # why it going wrong without json dumps, i don t get it (?)
        status=resp_code,
        mimetype='application/json'
    )
    return response
