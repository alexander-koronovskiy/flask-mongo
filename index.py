import traceback
from datetime import datetime

from flask import Flask, abort, json, request

from client_handler import convert_all_wrapper, convert_wrapper, index_wrapper
from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


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


# yaaaay i understood how i may organise err handle now
@app.route('/summary')
def summary():
    data = {'hello': 'kitty'}
    response = app.response_class(
        response=json.dumps(data),  # why it doesnt work without dumbs
        status=500,
        mimetype='application/json'
    )
    return response


@app.route('/convert', methods=['POST'])
def convert():
    result = {}
    try:
        from_rate_key = request.json.get('from')
        to_rate_key = request.json.get('to')
        origin_val = request.json.get('value')
    except KeyError:

        abort(500)

    else:
        if from_rate_key and to_rate_key:
            from_rate_key = from_rate_key.upper()
            to_rate_key = to_rate_key.upper()

            rates = convert_wrapper(cursor_rates().find_one())
            result = {'ur cash': {from_rate_key: origin_val},
                      'convert': {to_rate_key: origin_val * rates[to_rate_key] / rates[from_rate_key]}}
        else:

            abort(500)

    return result


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(e):
    print(e)
    full_trace = str(traceback.format_exc())
    return {'message': 'wrong rates convert parameters or app internal error',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'traceback': full_trace,
            }


if __name__ == '__main__':
    app.run()
