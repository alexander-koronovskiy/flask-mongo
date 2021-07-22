import requests


def test_convert_valid_single_json():
    data = {
        'from': 'usd',
        'to': 'eur',
        'value': 50
    }
    print(requests.post('http://127.0.0.1:5000/convert', data=data))
    assert True


def test_convert_invalid_key():
    pass


def test_convert_invalid_value():
    pass


def test_convert_valid_plural_json():
    pass


def test_convert_invalid_case_in_plural_json():
    pass
