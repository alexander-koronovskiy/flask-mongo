import traceback
from datetime import datetime

from flask import Flask

from db_handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    del_rates()
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = cursor_rates().find_one()  # clear code duplicate
    del rates['_id']  # need json serialize here
    return rates  # reformat json view


@app.route('/<rate_key>')
def rate_view(rate_key):
    rates = cursor_rates().find_one()
    del rates['_id']
    if rate_key in rates:
        return {rate_key: rates[rate_key]}
    else:
        return {rate_key: ''}


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())  # reformat json view
    return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'level': 'error', 'traceback': full_trace}, 404


if __name__ == '__main__':
    app.run()
