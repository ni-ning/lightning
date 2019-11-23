`闪电` 项目是平时实践技术总结，一个一个小轮子推着你前进
 
#####[alpha](https://github.com/ni-ning/lightning/tree/master/alpha) - 分布式消息队列 celery

##### [beta](https://github.com/ni-ning/lightning/tree/master/beta) - 自定义信号
```bash
# event_bus.py 自定义信号 signal
beta_signal_commit_event.send(sync_data)
beta_signal_commit_event.connect(handle)
```

##### [gamma](https://github.com/ni-ning/lightning/tree/master/gamma) - 命令行参数解析
```sh
python gamma/cmd.py linda 28 -d --female
```
