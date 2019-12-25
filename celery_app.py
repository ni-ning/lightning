# -*-coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.signals import after_task_publish, celeryd_after_setup

app = Celery('celery_alpha_main')
app.config_from_object('alpha.config.celery')


@after_task_publish.connect(sender='alpha.tasks.basic_task.add')
def task_sent_handler(sender=None, headers=None, body=None, **kw):

    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(info=info, ))


@celeryd_after_setup.connect
def setup_direct_queue(*arg, **kw):
    print('setup_direct_queue arg: %s, kw: %s' % (arg, kw))