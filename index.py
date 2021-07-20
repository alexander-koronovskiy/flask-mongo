import traceback
from datetime import datetime

from flask import Flask, abort

from client_handler import convert_all_wrapper, convert_wrapper, index_wrapper
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    return index_wrapper(cursor_rates().find_one())


@app.route('/<to_rate_key>')
@app.route('/<to_rate_key>/')
def convert_all(to_rate_key):
    rates = cursor_rates().find_one()
    if to_rate_key in rates:
        return convert_all_wrapper(rates, to_rate_key)
    else:
        return abort(404)


@app.route('/<from_rate_key>/<to_rate_key>')
def convert(from_rate_key, to_rate_key):
    rates = cursor_rates().find_one()
    if from_rate_key and to_rate_key in rates:
        return convert_wrapper(rates, from_rate_key, to_rate_key)
    else:
        return abort(404)


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())
    return {'message': 'wrong rates convert parameters',
            'response': 404,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'traceback': full_trace,
            }, 404


# add json handler of conn failure here

if __name__ == '__main__':
    app.run()
