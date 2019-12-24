# -*-coding:utf-8 -*-

from celery.schedules import crontab

include = ('alpha.tasks.basic_task',
           'alpha.tasks.bound_task',
           'alpha.tasks.schedule',
           'alpha.ops')

broker_url = 'pyamqp://guest@127.0.0.1//'
result_backend = 'redis://127.0.0.1'

enable_utc = False
timezone = 'Asia/Shanghai'

worker_redirect_stdouts_level = 'DEBUG'


# 周期性任务配置
beat_schedule = {
    'alpha.tasks.schedule.periodic_func': {
            'task': 'alpha.tasks.schedule.periodic_func',
            'schedule': crontab(minute='*/1'),
            'args': ('linda', ),
            'kwargs': {'age': 20}
        },
}