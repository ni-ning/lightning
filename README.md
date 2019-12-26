`闪电` 项目是平时实践技术总结，一个一个小轮子推着你前进
 
#### [alpha](https://github.com/ni-ning/lightning/tree/master/alpha) - 消息队列
```
lightning
    |- alpha 
        |- config/celery.py # celery配置
        |- rabbitmq         # rabbitmq示例
        |- tasks/           # 各类celery任务
    |- celery_app.py        # celery实例启动入口
```

- Celery - Distributed Task Queue
- Kombu
- RabbitMQ

#### [beta](https://github.com/ni-ning/lightning/tree/master/beta) - 自定义信号

```bash
# event_bus.py 自定义信号 signal
beta_signal_commit_event.send(sync_data)
beta_signal_commit_event.connect(handle)
```

#### [gamma](https://github.com/ni-ning/lightning/tree/master/gamma) - 命令行参数解析
```sh
python gamma/cmd.py linda 28 -d --female
```

#### [delta](https://github.com/ni-ning/lightning/tree/master/delta) - 定义网络日志

```bash
# 安装 python 依赖
pip install fluent-logger

# Fluentd daemon 日志采集服务器
docker run [options] fluentd
```
#### [epsilon](https://github.com/ni-ning/lightning/tree/master/epsilon) - 钉钉小程序
```
# 钉钉小程序登录
GET http://localhost/api/v1/epsilon/ding/login

# 后端自动处理登录后 userid 业务逻辑
POST http://localhost/api/v1/epsilon/ding/list
```