# -*-coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery_alpha_main')
app.config_from_object('config.celery_config')

