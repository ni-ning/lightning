# -*-coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery-alpha',
             include=['tasks.operation'],
             broker='pyamqp://guest@127.0.0.1//',
             backend='redis://127.0.0.1')

# app.config_from_object('config.celery_config')


