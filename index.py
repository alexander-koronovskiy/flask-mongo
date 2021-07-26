from flask import Flask, abort, request

from client_handler import (
    convert_all_wrapper,
    convert_wrapper,
    err_json_report,
    index_wrapper,
)
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
    abort(404)


@app.route('/convert', methods=['POST'])
def convert():
    result = err_json_report(app, 400)

    from_rate_key = request.json.get('from')
    to_rate_key = request.json.get('to')
    origin_val = request.json.get('value')

    if from_rate_key and to_rate_key and origin_val:
        from_rate_key = from_rate_key.upper()
        to_rate_key = to_rate_key.upper()
        result = convert_wrapper(rates=cursor_rates().find_one(),
                                 from_=from_rate_key,
                                 to_=to_rate_key,
                                 value_=origin_val)

    return result


# add err global handler here
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(e):
    resp_code = int(e.get_response().status[:3])  # how i can handle that on another ways (?)
    return err_json_report(app, resp_code)


if __name__ == '__main__':
    app.run()  # add logic sep in client handler
