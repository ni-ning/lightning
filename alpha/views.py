# -*-coding:utf-8 -*-

import logging
from flask import Blueprint, request, jsonify

alpha = Blueprint('alpha', __name__)
logger = logging.getLogger(__name__)


@alpha.route('/index', methods=['GET', 'POST'])
def index():
    data = dict(request.args) if request.method == 'GET' \
        else request.get_json(force=True, silent=True)
    logger.info('get data from request: %s' % data)
    return jsonify(data)
