from handler_db import cursor_rates, db_conn, del_rates, update_rates

PREV_COUNT = cursor_rates().count()


def test_db_conn():
    assert db_conn('rates')


def test_cursor_rates():
    assert cursor_rates()  # print .find_one() for pytest -s


def test_update_rates():
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    assert cursor_rates().find_one()


def test_del_rates():
    del_rates()
    assert PREV_COUNT == cursor_rates().count()  # original cond check
