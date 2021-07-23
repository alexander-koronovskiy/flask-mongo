import index

# i m test without func-template for code reduct of testing


def test_convert_valid_single_json():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'from': 'usd',
            'to': 'eur',
            'value': 50
        })
        assert response.status_code == 200
        assert 'convert' in response.get_json()


def test_convert_invalid_key():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'fr%%%': 'usd',
            'to': 'eur',
            'value': 50
        })
        assert response.status_code == 500
        assert 'message' in response.get_json()


def test_convert_invalid_value():
    index.app.config['TESTING'] = True
    with index.app.test_client() as client:
        response = client.post('/convert', json={
            'fr': 'usd',
            'to': 'eur',
            'value': 20
        })
        assert response.status_code == 500
        assert 'message' in response.get_json()


def test_convert_valid_plural_json():
    pass


def test_convert_invalid_case_in_plural_json():
    pass
