# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import time
from celery_app import app


# Celery support catching all states changes by setting on_message callback.
# @app.task(bind=True)
# def hello(self, x, y):
#     time.sleep(5)
#     self.update_state(state='PROGRESS', meta={'progress': 50})
#     time.sleep(5)
#     self.update_state(state='PROGRESS', meta={'progress': 90})
#     time.sleep(3)
#     return 'hello world: %i' % (x + y)


@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)


def on_raw_message(body):
    print(body)



