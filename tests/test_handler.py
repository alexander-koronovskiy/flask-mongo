from handler import get_outside_rates


def test_get_outside_rates():
    rates = get_outside_rates("https://www.cbr-xml-daily.ru/latest.js", "rates")
    for key in rates:
        assert key, rates[key]
