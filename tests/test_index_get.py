import requests


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()


def test_page_not_found():
    assert 'message' in requests.get('http://127.0.0.1:5000/USD/info').json()


def test_rate_view_valid_keys():
    rate_key_1 = 'RUB'
    rate_key_2 = 'USD'
    assert not requests.get(f'http://127.0.0.1:5000/{rate_key_1}').json()['rates'] == \
           requests.get(f'http://127.0.0.1:5000/{rate_key_2}').json()['rates']


def test_rate_view_invalid_keys():
    assert 'message' in requests.get('http://127.0.0.1:5000/доллар').json()
