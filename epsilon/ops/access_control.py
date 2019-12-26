# -*- coding: utf-8 -*-
'''
钉钉小程序登录认证
'''

from flask import session
from utils.api import APIResult


class DingLoginRequired(object):

    def __init__(self, view):
        super(DingLoginRequired, self).__init__()
        self.view = view
        self.__name__ = self.view.__name__

    def __get__(self, instance, owner):

        def decorator(*args, **kwargs):
            if not get_3rd_session():
                return APIResult(1)
            return self.view(instance, *args, **kwargs)
        return decorator

    def __call__(self, *args, **kwargs):
        if not get_3rd_session():
            return APIResult(1)
        return self.view(*args, **kwargs)


def get_3rd_session():
    token = gen_3rd_session()
    if not token:
        return None
    return session.get(token)


def gen_3rd_session():
    return 'ding_app_session'
