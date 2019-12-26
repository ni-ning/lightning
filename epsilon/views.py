# -*-coding:utf-8 -*-

import logging
from flask import Blueprint, request, session

from epsilon.ops import ding, access_control
from utils.api import api_wrap, APIResult

epsilon = Blueprint('epsilon', __name__)
logger = logging.getLogger(__name__)


@epsilon.route('/ding/login', methods=['GET'])
@api_wrap
def code2session():
    code = request.GET.get('code')
    if not code:
        return APIResult(code=1)

    code, msg = ding.get_user_info(code)
    if code != 0:
        return APIResult(code, msg=msg)
    session_key = access_control.gen_3rd_session()
    session[session_key] = msg
    return APIResult(code=0)


@epsilon.route('ding/list', methods=['POST'])
@access_control.DingLoginRequired
def ding_list():
    value = access_control.get_3rd_session() or {}
    user_id = value.get('userid')
    if not user_id:
        return APIResult(1, '需重新登录小程序')
    # user_id 逻辑处理
    return APIResult(0)
