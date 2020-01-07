# -*-coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_logger

from alpha.celery_app import app


logger = get_logger(__name__)


@app.task
def periodic_func(name, age=18):
    logger.info('name: %s, age: %s' % (name, age))
