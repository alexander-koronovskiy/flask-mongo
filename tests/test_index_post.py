import json

import index

valid_json = {'from': 'rub', 'to': 'eur', 'value': 50}
invalid_key = {'fr%%%': 'usd', 'to': 'eur', 'value': 50}
invalid_value = {'from': 'usduuu', 'to': 'eur', 'value': 707}


def testing_func_schema(req: json) -> json:
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json=req)
    return response


def test_convert_valid_json():
    assert 'convert' in testing_func_schema(valid_json).get_json()


def test_convert_invalid_key():
    assert not testing_func_schema(invalid_key).get_json()  # empty here


def test_convert_invalid_value():
    assert 'message' in testing_func_schema(invalid_value).get_json()  # key error here

# handle empty responses, key error, logic sep in client handler,
# fix resp in index tests file
