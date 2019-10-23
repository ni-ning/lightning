# -*-coding:utf-8 -*-
import datetime
from celery_app import app


def async_calc(x, y):
    calc.apply_async(args=(x, y), kwds={'verbose': 'Hello world!'})


@app.task
def calc(x, y, verbose=None):
    print('start calc: %s' % str(datetime.datetime.now()))
    if verbose:
        print(verbose)
    ret = x + y
    print('%s + %s = %s' % (x, y, ret))
    return ret
