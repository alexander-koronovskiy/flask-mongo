from flask import Flask

from handler import emergency_rates_to_client

app = Flask(__name__)


@app.route('/')
def index():
    return emergency_rates_to_client()


if __name__ == '__main__':
    app.run()
