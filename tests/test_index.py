import requests


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()


def test_page_not_found():
    assert 'traceback' in requests.get('http://127.0.0.1:5000/USD/info').json()


def test_rate_view_valid_keys():
    rate_key_1 = 'RUB'
    rate_key_2 = 'USD'
    assert not requests.get(f'http://127.0.0.1:5000/{rate_key_1}').json()['rates'] == \
           requests.get(f'http://127.0.0.1:5000/{rate_key_2}').json()['rates']


def test_rate_view_invalid_keys():
    assert 'traceback' in requests.get('http://127.0.0.1:5000/доллар').json()


def test_rate_convert_valid_keys():
    from_rate_key = 'EUR'
    to_rate_key = 'USD'
    assert 'rates' in requests.get(f'http://127.0.0.1:5000/{from_rate_key}/{to_rate_key}').json()


def test_rate_convert_invalid_keys():
    assert 'traceback' in requests.get('http://127.0.0.1:5000/USD/рубль').json()
