import traceback
from datetime import datetime

from flask import Flask, render_template

from handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = cursor_rates().find_one()
    del_rates()
    del rates['_id']
    return rates


@app.errorhandler(404)
def page_not_found(e):
    full_trace = str(traceback.format_exc())
    return {'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'level': 'error', 'traceback': full_trace}, 404


if __name__ == '__main__':
    app.run()  # add min error handler for index (?)
