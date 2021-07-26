import index

# handle empty responses, key error
# testing func schema realise


def test_convert_valid_single_json():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'from': 'usd',
            'to': 'eur',
            'value': 50
        })
        assert 'convert' in response.get_json()


def test_convert_invalid_key():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'fr%%%': 'usd',
            'to': 'eur',
            'value': 50
        })
        assert not response.get_json()  # empty here


def test_convert_invalid_value():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'from': 'usduuu',
            'to': 'eur',
            'value': 707
        })
        assert 'message' in response.get_json()  # key error here
