import json
from datetime import datetime

import flask


def err_json_report(app: flask.app, resp_code: int) -> json:
    """json err log builder for bad get or post requests"""
    data = {'message': 'wrong rates convert parameters or app internal error',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    response = app.response_class(
        response=json.dumps(data),  # why it going wrong without json dumps, i don t get it (?)
        status=resp_code,
        mimetype='application/json'
    )
    return response
