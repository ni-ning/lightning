# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery.task import Task

from celery_app import app


class MyTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@app.task(base=MyTask)
def add(x, y):
    return KeyError()




