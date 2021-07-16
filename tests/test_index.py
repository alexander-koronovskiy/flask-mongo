import requests

# add json parse in methods


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()


def test_page_not_found():
    assert requests.get('http://127.0.0.1:5000/smth/smth').json()
