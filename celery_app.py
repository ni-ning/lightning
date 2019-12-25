# -*-coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
from celery import Celery, Task
from celery.signals import after_task_publish, celeryd_after_setup
from celery.utils.log import get_logger

from lightmail import send_email

logger = get_logger(__name__)

app = Celery('celery_alpha_main')
app.config_from_object('alpha.config.celery')


class CeleryTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))
        notifier = ['nining1314@gmail.com']
        if notifier:
            title = "%s alpha celery exception" % str(datetime.datetime.now())[:19]
            email_body = "celery tasks failed : "
            email_body += "\ntask_id : %s" % task_id
            email_body += "\ntraceback :"
            email_body += "\n%s\n" % einfo.traceback
            email_body = ('<p>%s</p>' % email_body).replace('\n', '<br\>')
            send_email(notifier, content=email_body, title=title)


@after_task_publish.connect(sender='alpha.tasks.basic_task.add')
def task_sent_handler(sender=None, headers=None, body=None, **kw):

    info = headers if 'task' in headers else body
    logger.info('after_task_publish for task id {info[id]}'.format(info=info, ))


@celeryd_after_setup.connect
def setup_direct_queue(*arg, **kw):
    logger.info('setup_direct_queue arg: %s, kw: %s' % (arg, kw))