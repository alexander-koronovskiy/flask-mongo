import json

from flask import Flask
from jsonschema import validate

from handler import db_conn, record_outside_rates

app = Flask(__name__)

# expected json
schema = {
    'type': 'object',
    'properties': {
        'description': {'type': 'string'},
        'status': {'type': 'boolean'},
        'value_a': {'type': 'number'},
        'value_b': {'type': 'number'},
    },
}


@app.route('/')
def index():
    my_json = json.loads('{"description": "Hello world!", "status": true, "value_a": 1, "value_b": 3.14}')
    validate(instance=my_json, schema=schema)
    return my_json


if __name__ == '__main__':
    app.run(debug=True)
