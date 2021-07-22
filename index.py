
import traceback
from datetime import datetime

from flask import Flask, abort, request

from client_handler import convert_all_wrapper, convert_wrapper, index_wrapper
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


# add a connection error and status 500 handlers
# refract error handlers and convert method

@app.route('/', methods=['POST', 'GET'])
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    return index_wrapper(cursor_rates().find_one())


@app.route('/<to_rate_key>', methods=['GET'])
@app.route('/<to_rate_key>/', methods=['GET'])
def convert_all(to_rate_key):
    rates = cursor_rates().find_one()
    if to_rate_key in rates:
        return convert_all_wrapper(rates, to_rate_key)
    else:
        return abort(404)


@app.route('/convert', methods=['POST'])
def convert():

    # handle many json cases mb in cycles, refract that overcode - it s non pythonic

    result = {}
    try:
        from_rate_key = request.json.get('from')
        to_rate_key = request.json.get('to')
        origin_val = request.json.get('value')
    except KeyError:
        abort(400)
    else:
        if from_rate_key and to_rate_key:
            from_rate_key = from_rate_key.upper()
            to_rate_key = to_rate_key.upper()

            rates = convert_wrapper(cursor_rates().find_one())
            result = {'ur cash': {from_rate_key: origin_val},
                      'convert': {to_rate_key: origin_val * rates[to_rate_key] / rates[from_rate_key]}}
        else:
            abort(400)

    return result


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())
    return {'message': 'wrong rates convert parameters',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'traceback': full_trace,
            }, 404


if __name__ == '__main__':
    app.run()
