import json


# is that correct serialization objectId (?)
def json_handler(rates: json) -> json:
    rates['id'] = str(rates['_id'])
    rates['RUB'] = 1
    del rates['_id']
    return rates


# i think this methods is excess, i m use code from methods in index file

def error_response_handler():
    pass


def correct_response_handler():
    pass
