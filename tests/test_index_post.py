import json

import index

valid_json = {'from': 'rub', 'to': 'eur', 'value': 50}
invalid_key = {'fr%%%': 'usd', 'to': 'eur', 'value': 50}
invalid_value = {'from': 'usduuu', 'to': 'eur', 'value': 707}


def _func_schema(req: json) -> json:
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json=req)
    return response.get_json()


def test_convert_valid_json():
    assert 'convert' in _func_schema(valid_json)


def test_convert_invalid_key():
    assert 'message' in _func_schema(invalid_key)


def test_convert_invalid_value():
    assert 'convert' in _func_schema(invalid_value)
