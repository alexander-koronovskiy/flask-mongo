from flask import Flask

from handler import cursor_rates, del_rates, update_rates

app = Flask(__name__)


@app.route('/')
def index():
    update_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')
    rates = cursor_rates().find_one()
    del_rates()
    del rates['_id']
    return rates


if __name__ == '__main__':
    app.run()  # add min error handler for index (?)
