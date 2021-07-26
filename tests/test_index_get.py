import json

import index


def _func_schema(path: str) -> json:
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.get(path, follow_redirects=True)
    return response.get_json()


def test_index():
    assert 'rates' in _func_schema('/USD')


def test_page_not_found():
    assert 'message' in _func_schema('/tttt')


def test_rate_view_valid_key():
    assert 'rates' in _func_schema('/USD')
