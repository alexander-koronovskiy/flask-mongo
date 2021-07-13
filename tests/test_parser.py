from parser import parse_page


def test_parse_page():
    url = "https://markets.businessinsider.com/"
    assert parse_page(url)
