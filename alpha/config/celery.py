# -*-coding:utf-8 -*-

from kombu import Queue, Exchange, binding
from celery.schedules import crontab

include = ('alpha.tasks.basic_task',
           'alpha.tasks.bound_task',
           'alpha.tasks.schedule',
           'alpha.ops')

broker_url = 'pyamqp://guest@127.0.0.1//'
# broker_url = 'librabbitmq://guest@127.0.0.1//'
result_backend = 'redis://127.0.0.1'

enable_utc = False
timezone = 'Asia/Shanghai'

worker_redirect_stdouts_level = 'DEBUG'

# If enabled(default), any queues specified that aren't defined in task_queues
# will be automatically created.
task_create_missing_queues = True

# a list of Queue instances
media_exchange = Exchange('media', type='direct')
task_queues = (
    Queue('tianfu-gbm-celery-task-main',
          exchange=Exchange('tianfu-gbm-celery-task-main', type='direct'),
          routing_key='tianfu-gbm-celery-task-main'),
    Queue('videos', exchange=media_exchange, routing_key='media.video'),
    Queue('images', exchange=media_exchange, routing_key='media.image')
)

# multiple bindings to a single queue
# task_queues = (
#     Queue('media', [
#         binding(media_exchange, routing_key='media.video'),
#         binding(media_exchange, routing_key='media.image'),
#     ])
# )

# 默认队列名 celery -> default
task_default_queue = 'tianfu-gbm-celery-task-main'
task_default_exchange = 'tianfu-gbm-celery-task-main'
task_default_routing_key = 'tianfu-gbm-celery-task-main'
task_default_exchange_type = 'direct'

# 路由配置，and override this using the routing_key argument to Task.apply_async()
# task_routes = {
#         'media.tasks.video': {
#             'queue': 'videos',
#             'routing_key': 'media.video',
#         },
#         'media.tasks.image': {
#             'queue': 'images',
#             'routing_key': 'media.image',
#         },
# }

# 周期性任务配置
beat_schedule = {
    'alpha.tasks.schedule.periodic_func': {
            'task': 'alpha.tasks.schedule.periodic_func',
            'schedule': crontab(minute='*/1'),
            'args': ('linda', ),
            'kwargs': {'age': 20}
        },
}