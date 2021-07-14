from flask import Flask

from handler import post_json_to_client, temp_data

app = Flask(__name__)


@app.route('/')
def index():
    return post_json_to_client(temp_data)


if __name__ == '__main__':
    app.run(debug=True)  # it s just works with test json
