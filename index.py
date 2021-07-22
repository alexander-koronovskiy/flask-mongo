# python libs
import traceback
from datetime import datetime

# libs from requirements
from flask import Flask, abort, request

# my libs
from client_handler import convert_all_wrapper, convert_wrapper, index_wrapper
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    return index_wrapper(cursor_rates().find_one())
    # add a connection error handler


@app.route('/<to_rate_key>', methods=['GET'])
@app.route('/<to_rate_key>/', methods=['GET'])
def convert_all(to_rate_key):
    rates = cursor_rates().find_one()
    if to_rate_key in rates:
        return convert_all_wrapper(rates, to_rate_key)
    else:
        return abort(404)  # reformat page not found handler


@app.route('/convert', methods=['POST'])
def convert():

    # check that not empty
    from_rate_key = request.json.get('from').upper()
    to_rate_key = request.json.get('to').upper()
    origin_val = request.json.get('value')

    # handle keys

    # key error and value_error handle, uppercase key mod here

    rates = convert_wrapper(cursor_rates().find_one())
    return {'ur cash': {from_rate_key: origin_val},
            'convert': {to_rate_key: origin_val * rates[to_rate_key] / rates[from_rate_key]}}

    # how to handle many cases
    # add 405 handler


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())
    return {'message': 'wrong rates convert parameters',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'traceback': full_trace,
            }, 404


# add json handler of conn failure, 500 status etc here

if __name__ == '__main__':
    app.run()
