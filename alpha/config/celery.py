# -*-coding:utf-8 -*-

include = ('alpha.tasks.basic_task',
           'alpha.tasks.bound_task',
           'alpha.ops')

broker_url = 'pyamqp://guest@127.0.0.1//'
result_backend = 'redis://127.0.0.1'

enable_utc = False
timezone = 'Asia/Shanghai'

worker_redirect_stdouts_level = 'DEBUG'
