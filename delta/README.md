
## 理论基础
日志是一种可以追踪软件运行时所发生事件的方法
1. 日志的作用
- 程序调试  
- 了解软件程序运行情况，是否正常
- 软件程序运行故障分析与问题定位

2. 日志的等级
- 线下开发，尽可能详细查看程序运行状态，耗费机器性能
- 线上运行，只记录异常、错误信息等，减小服务器压力


| 级别      |      描述         | 
| --------  | --------          |
| DEBUG     | 最详细的日志信息  | 
| INFO      | 关键节点信息      |
| WARNING   | 警告(如磁盘快满了)|
| ERROR     | 某些功能不能运行  |
| CRITICAL  | 软件程序不能运行  |

DEBUG < INFO < WARNING < ERROR < CRITICAL 级别依次升高  
当程序指定某个级别后，程序会记录所有日志级别大于或等于指定日志级别的日志信息

3. 日志的格式
- 事件发生时间
- 事件发生位置
- 事件级别
- 时间内容

4. 日志的实现

几乎所有开发语言都会内置日志相关功能, Python 标准模块 -- logging

## Python实现模块 logging

logging相比print，具备有点
- 设置等级，区分线上和线下输出信息
- print只能输出到标准输出中，logging设置输出去向

1. logging使用方式
- 第一种方式是使用logging提供的模块级别的函数
- 第二种方式是使用Logging日志系统的四大组件

##### 第一种使用方式：简单配置
```
import logging
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
DATE_FORMAT = '%Y-%m-%d %X'

logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)

logging.debug('debug_msg')
logging.info('info_msg')
logging.warning('warning_msg')
logging.error('error_msg')
logging.critical('critical_msg')
```

##### 第二种使用方式：日志流处理流程

logging日志模块四大组件
| 组件名称 | 对应类名  | 功能描述 |
| -------- | --------  | -------- |
| 日志器   | Logger    | 提供了应用程序可一直使用的接口 |
| 处理器   | Handler   | 将logger创建的日志记录发送到合适的目的输出|
| 过滤器   | Filter    | 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录|
| 格式器   | Formatter | 决定日志记录的最终输出格式|

这些组件之间的关系描述
- 日志器(Logger)需要通过处理器(Handler)将日志信息输出到目标位置，如文件、sys.stdout、网络等
- 不同的处理器(Handler)可以将日志输出到不同的位置
- 日志器(Logger)可以设置多个处理器(Handler)将同一条日志记录输出到不同的位置
- 每个处理器(Handler)都可以设置自己的过滤器(Fliter)实现日志过滤，从而只保留感兴趣的日志
- 每个处理器(Handler)都可以设置自己的格式器(Formatter)，从而实现不同的日志格式



![logging](https://github.com/ni-ning/lightning/images/delta/logging.png)

```
import logging

# 创建logger, 如参数为空返回root logger
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# 创建handler
fh = logging.FileHandler('log.log', encoding='utf-8')
sh = logging.StreamHandler()

# 设置输出格式
formatter = logging.Formatter(fmt="%(asctime)s %(filename)s %(message)s",datefmt="%Y/%m/%d %X")

# 为handler指定输出格式
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# 为logger添加日志处理器
logger.addHandler(fh)
logger.addHandler(sh)

# 输出不同级别日志
logger.debug("debug_msg")
logger.info("info_msg")
logger.warning("warning_msg")
logger.error("error_msg")
logger.critical("critical_msg")
```

注意：
1. 封装函数生成logger时，要注意多次绑定 addHandler问题
2. getLogger 路径名 全局字典 层级结构 配置继承
3. 

## 日志网络发送 fluent-logger和fluentd
Fluentd daemon 日志采集服务器，fluent-logger发送日志到日志采集服务器上
![fluent](https://github.com/ni-ning/lightning/images/delta/fluent.png)



1. Python端 安装 pip install fluent-logger
2. Ubuntu端 安装 docker run fluentd

```
# 前期准备
sudo groupadd fluent
sudo usermod -G fluent $USER

# docker 部署 fluentd
docker run -p 24224:24224 -p 24224:24224/udp -v /var/log/fluentd/data:/fluentd/log --name fluent -u fluent fluentd
sudo chmod a+w /var/log/fluentd/data

# 查看日志
docker logs fluent
cd /var/log/fluentd/data
```

#### 发送示例
```
pip install fluent-logger

from fluent import sender
logger = sender.FluentSender('gbm', host='127.0.0.1', port=24224)
logger.emit('custom', {'from': 'userA', 'to': 'userB'})
```

#### 项目实践

公共库中定义 gsutil/fluent_log.py

```
import logging
import traceback
from fluent import sender

SETUP_STATES = {'done': False}

class FluentTaggedHandler(logging.Handler):
    def __init__(self, base_tag, host="localhost", port=24224, timeout=1):
        logging.Handler.__init__(self)
        self.sender = sender.FluentSender(base_tag, host=host, port=port, timeout=timeout)
    def emit(self, record):
        content = record.getMessage()
        if record.exc_info:
            tb = traceback.format_exception(*record.exc_info)
            content = '%s\n%s' % (content, ''.join(tb))
        return self.sender.emit(record.name, content)


def setup_fluent(base_tag, host="localhost", port=24224, timeout=1, level=logging.INFO):
    '''
    setup root logger to a fluent handler.
    '''
    if SETUP_STATES['done']:
        return False
    SETUP_STATES['done'] = True
    handler = FluentTaggedHandler(base_tag, host=host, port=port, timeout=timeout)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(level)
    return True
```

线上项目 gbm/conf.py

```
import gsutil.fluent_log
gsutil.fluent_log.setup_fluent('base_tag', host='127.0.1', port=24224)
```





## 参考链接
1. [Fluentd 官网](https://www.fluentd.org/)
2. [fluent-logger PyPI](https://pypi.org/project/fluent-logger/)
3. [logger 博客理论](https://www.cnblogs.com/Nicholas0707/p/9021672.html)
4. [logging 库最好的一篇文章](https://juejin.im/post/5bc2bd3a5188255c94465d31)
4. [logging PEP 说明](https://www.python.org/dev/peps/pep-0282/)
5. [Docker 从入门到实践](https://yeasy.gitbooks.io/docker_practice/)





