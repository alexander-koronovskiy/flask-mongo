from parser import get_exchange_rate, parse_page


def test_parse_page():
    url = "https://markets.businessinsider.com/"
    assert parse_page(url)


def test_get_exchange_rate():
    url = f"https://randomuser.me/api/?results=5"
    assert get_exchange_rate(url)
