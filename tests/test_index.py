import requests


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()


def test_page_not_found():
    assert requests.get('http://127.0.0.1:5000/USD/info').json()


def test_rate_view_valid_key():
    rate_key = 'EUR'
    assert requests.get(f'http://127.0.0.1:5000/{rate_key}').json()['value']


def test_rate_view_invalid_key():
    rate_key = 'EURыыыыы'
    assert not requests.get(f'http://127.0.0.1:5000/{rate_key}').json()[rate_key]
