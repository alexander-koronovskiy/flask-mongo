from handler import cursor_rates, db_conn, del_rates, update_rates


def test_db_conn():
    assert db_conn('rates')


def test_cursor_rates():
    assert cursor_rates()  # print .find_one() for pytest -s


def test_update_rates():
    before_upd_count = cursor_rates().count()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    after_upd_count = cursor_rates().count()
    assert before_upd_count - after_upd_count


def test_del_rates():
    del_rates()
    assert not cursor_rates().count()


# make jsonful check
def test_jsonful_data_to_client():
    import requests
    assert requests.get('https://www.cbr-xml-daily.ru/latest.js').json()['rates']
