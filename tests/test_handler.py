from handler import get_outside_rates_old


def test_get_outside_rates_old():
    rates = get_outside_rates_old('https://www.cbr-xml-daily.ru/latest.js')['rates']
    for key in rates:
        assert key, rates[key]
