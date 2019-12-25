# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from celery_app import app, CeleryTask


@app.task(base=CeleryTask)
def error():
    return KeyError()




