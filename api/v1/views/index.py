#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    status_dict = {'status': 'OK'}
    return jsonify(status_dict), 200

