# -*-coding:utf-8 -*-
import datetime
import logging
from celery_app import app

logger = logging.getLogger(__name__)


def async_calc(x, y):
    calc.apply_async(args=(x, y), kwds={'verbose': 'Hello world!'})


@app.task
def calc(x, y, verbose=None):
    logger.info('start calc: %s' % str(datetime.datetime.now()))
    if verbose:
        print(verbose)
    ret = x + y
    logger.info('%s + %s = %s' % (x, y, ret))
    logger.info('end calc: %s' % str(datetime.datetime.now()))
    return ret
