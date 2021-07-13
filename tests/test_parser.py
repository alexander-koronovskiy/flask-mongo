from parser import get_exchange_rate


def test_get_exchange_rate():
    rates = get_exchange_rate("https://www.cbr-xml-daily.ru/latest.js", "rates")
    for key in rates:
        assert key, rates[key]
