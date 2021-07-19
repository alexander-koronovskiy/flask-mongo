import traceback
from datetime import datetime

from flask import Flask

from client_handler import json_handler
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
@app.route('/RUB')
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = json_handler(cursor_rates().find_one())
    return rates


@app.route('/<rate_key>')  # realise /<from>/<to> case
def rate_view(rate_key):
    rates = json_handler(cursor_rates().find_one())
    if rate_key in rates:

        return {
                    'from': rate_key,
                    'to': 'RUB',
                    'value': rates[rate_key]
        }

    else:
        return {rate_key: ''}  # raise here some exception for example


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())  # need particular func for exception handle
    return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'level': 'error', 'traceback': full_trace}, 404


if __name__ == '__main__':
    app.run()
