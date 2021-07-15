import requests


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()

# add test of closed flask server case
