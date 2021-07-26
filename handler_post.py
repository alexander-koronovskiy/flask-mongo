import json

from handler_get import index_wrapper


def convert_wrapper(rates: json, from_: str, to_: str, value_: str) -> json:
    """json response formation for convert method"""
    rates = index_wrapper(rates)['rates']
    try:
        result = value_ * rates[to_] / rates[from_]
    except KeyError:
        result = 'wrong converter parameters'
    return {'ur cash': {from_: value_}, 'convert': {to_: result}}
