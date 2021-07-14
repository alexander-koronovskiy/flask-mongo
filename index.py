from flask import Flask

from handler import db_conn, record_outside_rates

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    # remove previous record
    db_conn('rates').rates.remove()  # refract remove() to another method

    # printing records from db
    rates = record_outside_rates('https://www.cbr-xml-daily.ru/latest.js', 'rates')  # use kw in func ???
    print(db_conn('rates').rates.find_one())
