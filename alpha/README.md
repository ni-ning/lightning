
#### What is celery
Celery 是一个使用 Python 开发的分布式任务调度模块
- task queue with focus on real-time processing
- supporting task scheduling

![celery](https://raw.githubusercontent.com/ni-ning/lightning/master/images/alpha/celery.png)


#### Choosing a Broker
```
# rabbitmq
docker run -it -d --name rabbitmq  \
-p 5672:5672 \
-p 5671:5671 \
-p 4369:4369 \
-p  25672:25672 \
rabbitmq

# redis
docker run -it -d --name redis -p 6379:6379 redis
```

#### Application
The Celery library must be instantiated before use, this instance is called an application(or app for short).


```
from celery import Celery

app = Celery()
app.config_from_object('alpha.config.celery')

@app.task
def add(x, y):
    return x + y
```

发送的消息，肯定不是执行的源码，而是 the name of the task you want execute，所以: every worker maintains a mapping of task names to their actual functions, called `task registry`

```
>>> add
<@task: __main__.add of __main__ at 0x7f742e752d30>
>>> add.name
'__main__.add'

>>> app.tasks['__main__.add']
<@task: __main__.add of __main__ at 0x7f742e752d30>
```
- 解决 __main__的问题 Celery('celery_alpha_main') 即可
- config can change how Celery works, 如 app.conf

```
>>> type(add)
celery.local.PromiseProxy
```
- add 惰性机制，只有执行的时候才创建
- the best practice is to always pass the app instance around to anything that needs it


#### Tasks
A task is a class that can be created out any callable. 承担两个角色
- what happens when a task is called(sends a message)
- what happens when a worker receives that message

```
from celery_app import app

@app.task(bind=True)
def hello(self, x, y):
    return x + y
```

#### Calling Tasks

Celery has uniform "Calling API" used by task instances

- T.delay(arg, kwarg=value) 快捷方式
- T.apply_async((arg, ), {'key': value})
- T.apply_async(countdown=10) executes in 10 seconds from now
- T.apply_async(eta=now + timedelta(seconds=10) executes in 10 seconds from now, specified using eta
- T.apply_async(countdown=60, expires=120) executes in one minute from now, but expires after 2 minutes
- T.apply_async(expires=now + timedelta(days=2) expires in 2 days, set using datetime
- T() will not be executed by a worker, but in the current process


```
>>> add.OperationError
kombu.exceptions.OperationalError
```
- 神奇操作异常绑定到 add 上

```
add.apply_async((10, 10), serializer='json')
```
- Data transferred between clients and workers needs to be serialized.

```
add.apply_async((100, 200), queue='priority.high')
```
- Celery can route tasks to different queues.

Advanced options are for users who want to take use of AMQP's full routing capabilities.
- exchange
- routing_key
- priority


#### Workers Guide

```
# Starting the worker, 结合 docker 二级命令行
celery worker --help
celery worker -A celery_app --loglevel=info  --concurrency=`count of default cpu`

# Stopping the worker 
ps auxww | grep 'celery worker'   # ??? 疑问为啥 2 个 celery
pkill -9 -f 'celery worker'
```

查看信息

```
celery inspect -A celery_app active_queues
celery inspect -A celery_app stats
```


#### Periodic Tasks

```
# alpha/config/celery.py 增加周期性配置项
beat_schedule = {
    'alpha.tasks.schedule.periodic_func': {
            'task': 'alpha.tasks.schedule.periodic_func',
            'schedule': crontab(minute='*/1'),
            'args': ('linda', ),
            'kwargs': {'age': 20}
        },
}

# Development Environment
celery worker -A celery_app --loglevel=info -B

# Production Environment
celery beat -A celery_app --loglevel=info
```

#### Routing Tasks

**Messages**
```
{'task': 'myapp.tasks.add',
 'id': '54086c5e-6193-4575-8308-dbab76798756',
 'args': [4, 4],
 'kwargs': {}}
```
- A message consists of headers and a body

**Produces, consumers, and brokers**
- The client sending messages is typically called a publisher, or a producer
- The entity receiving messages is called a consumper
- The broker is the message sever, routing messages from producers to consumers.

**Exchanges, queues, and routing keys**

1. Create an exchange, which routes messages to one or more queues
2. Create a queue
3. Bind the queue to the exchange

**Exchange types**

The exchange type defines how the messages are routed through the exchange.
- direct exchanges match by exact routing keys, so a queue bound by the routing key `video` only receives messages with that routing key
- topic exchanges match routing keys using dot-separated words, and the wild-card charaters: * (matches a single word), and # (matches zero or more words)

后续 AMQP 需要详细了解


#### Monitoring and Management Guide

```
celery inspect --help

# flower 需要安装 http://127.0.0.1:5555
pip install flower
celery flower -A celery_app --port=5555

# events 内置
celery events -A celery_app
```



#### Security
- Areas of Concern: Broker, Client, Worker
- Serializers
- Message Signing

#### Optimizing
- librabbitmq 会抛异常，待定
- Using Transient Queues, 特定场景不需要持久化message
- worker_prefetch_multiplier = 1

#### Debugging
an extended version of pdb
```
from celery.contrib import rdb
```

#### Concurrency
about Eventlet

#### Signals
Several kinds of events trigger signals, you can connect to these signals to perform actions as they trigger.

#### Configuration and defaults

#### Kombu

Kombu is a messaging library for Python.
- AMQP the Advanced Message Queuing Protocol
- RabbitMQ the most popular implementation


#### 参考链接
- [使用 Celery 踩过的坑](https://juejin.im/entry/589a8c6586b599006b1ae4b1)
- [官网 User Guide](http://docs.celeryproject.org/en/latest/userguide/index.html)
- [官网 Community](http://www.celeryproject.org/community/)
- [官网 celeryproject.org](http://www.celeryproject.org/)