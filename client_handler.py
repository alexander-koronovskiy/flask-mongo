import json


# handle json data here, serialize ObjectId, add {"RUB": 1}
def json_handler(rates: json) -> json:
    del rates['_id']
    return rates


def error_handler():
    pass
