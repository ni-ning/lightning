# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from celery_app import app


@app.task(bind=True)
def add(self, x, y):
    logging.info(self.request.id)
    return x + y

