import json


# is that correct serialization objectId (?)
def json_handler(rates: json) -> json:
    rates['id'] = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']
    return rates


def error_response_handler():
    pass


def success_response_handler():
    pass
