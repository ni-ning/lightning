# -*-coding:utf-8 -*-

import logging
from flask import Blueprint, request

from omega.ops import func
from utils.api import api_wrap, APIResult

omega = Blueprint('omega', __name__)
logger = logging.getLogger(__name__)


@omega.route('/index', methods=['GET', 'POST'])
@api_wrap
def index():
    data = dict(request.args) if request.method == 'GET' \
        else request.get_json(force=True, silent=True)
    logger.info('get data from request: %s' % data)
    func()  # 业务逻辑
    return APIResult(code=0, result=data)
