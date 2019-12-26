# -*- coding:utf-8 -*-
'''
与钉钉服务通信
https://pypi.org/project/dingtalk-sdk/
https://ding-doc.dingtalk.com/doc#/dev/wcoaey
'''

import logging
from dingtalk.core.exceptions import DingTalkClientException

from epsilon.meta import client

logger = logging.getLogger(__name__)


def get_user_info(code):
    '''
    请求钉钉正常返回结果
    {
        "userid": "****",
        "sys_level": 1,
        "errmsg": "ok",
        "is_sys": true,
        "errcode": 0
     }
    '''
    try:
        result = client.user.getuserinfo(code)
        return 0, result
    except DingTalkClientException as e:
        logger.error(str(e.errmsg))
        return 1, str(e.errmsg)
