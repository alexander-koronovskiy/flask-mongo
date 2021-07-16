import requests


def test_index():
    assert requests.get('http://127.0.0.1:5000/').json()


def test_404():
    assert requests.get('http://127.0.0.1:5000/wrongpath404').status_code == 404
