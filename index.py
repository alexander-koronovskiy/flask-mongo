import traceback
from datetime import datetime

from flask import Flask

from client_handler import json_handler
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = json_handler(cursor_rates().find_one())
    return rates


# realise rates to_rate_key


@app.route('/<from_rate_key>/<to_rate_key>')
def rate_view(from_rate_key, to_rate_key):
    rates = json_handler(cursor_rates().find_one())
    if from_rate_key and to_rate_key in rates:

        return {
                    'from': from_rate_key,
                    'to': to_rate_key,
                    'value': rates[to_rate_key] / rates[from_rate_key]
        }

    else:
        return {'invalid_data': ''}  # raise here some exception for example


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())  # need particular func for exception handle
    return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'level': 'error', 'traceback': full_trace}, 404


if __name__ == '__main__':
    app.run()
