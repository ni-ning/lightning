# -*-coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from alpha.celery_app import app


@app.task(name='alpha.tasks.basic_task')
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
