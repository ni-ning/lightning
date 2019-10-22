# -*-coding:utf-8 -*-

include = ('tasks.operation', )

broker_url = 'pyamqp://guest@127.0.0.1//'
result_backend = 'redis://127.0.0.1'

enable_utc = False
timezone = 'Asia/Shanghai'
