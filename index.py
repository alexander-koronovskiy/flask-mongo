from flask import Flask

from handler import emergency_rates_to_client

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    print(emergency_rates_to_client())
    app.run()
