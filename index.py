import traceback
from datetime import datetime

from flask import Flask, abort

from client_handler import json_handler
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = json_handler(cursor_rates().find_one())
    return rates


@app.route('/<to_rate_key>')
@app.route('/<to_rate_key>/')
def rate_view(to_rate_key):
    rates = json_handler(cursor_rates().find_one())
    if to_rate_key in rates:
        return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'response': 200,
                'rates': rates  # need handle this
                }
    else:
        return abort(404)


@app.route('/<from_rate_key>/<to_rate_key>')
def rate_convert(from_rate_key, to_rate_key):
    rates = json_handler(cursor_rates().find_one())
    if from_rate_key and to_rate_key in rates:
        return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'response': 200,
                'rates': {'from': from_rate_key, 'to': to_rate_key,
                          'value': rates[to_rate_key] / rates[from_rate_key]}
                }
    else:
        return abort(404)


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())
    return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'response': 404, 'traceback': full_trace, 'message': 'wrong rates convert parameters'}, 404


if __name__ == '__main__':
    app.run()
