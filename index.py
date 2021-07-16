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
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()  # add min error handler for index (?)
