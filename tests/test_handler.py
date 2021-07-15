from handler import cursor_rates, db_conn, post_json_to_client, temp_data, update_rates


def test_db_conn():
    assert db_conn('rates')


def test_cursor_rates():
    print(cursor_rates().find_one())  # use -s in pytest for  state check
    assert cursor_rates()


def test_update_rates():
    before_upd_count = cursor_rates().count()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    after_upd_count = cursor_rates().count()
    assert before_upd_count - after_upd_count


def test_post_json_to_client():
    assert post_json_to_client(temp_data)
