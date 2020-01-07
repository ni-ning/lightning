# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import time
from alpha.celery_app import app


# Celery support catching all states changes by setting on_message callback.
@app.task(bind=True)
def hello(self, x, y):
    time.sleep(5)
    self.update_state(state='PROGRESS', meta={'progress': 50})
    time.sleep(5)
    self.update_state(state='PROGRESS', meta={'progress': 90})
    time.sleep(3)
    return 'hello world: %i' % (x + y)


def on_raw_message(body):
    print(body)


if __name__ == '__main__':
    # hello(100, 200) 就不要再调用了，会抛出异常
    r = hello.delay(100, 200)
    print(r.get(on_message=on_raw_message, propagate=False))

