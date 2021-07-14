from handler import db_conn, post_json_to_client, temp_data, update_rates


def test_db_conn():
    assert db_conn('rates')


# i m correcting this test yet
def test_update_rates():
    rates = update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    assert db_conn('rates').rates.find_one()


def test_post_json_to_client():
    assert post_json_to_client(temp_data)
