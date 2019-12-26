

# 钉钉平台介绍

#### 不同角色使用钉钉
- 普通用户 移动端或PC端
- 管理员 通过 [企业登录](https://oa.dingtalk.com/?spm=a3140.8196074.2231602.14.5a9e37fdhLBiP7#/login) 入口进入管理页面
- 开发者通过 [钉钉开放平台](https://ding-doc.dingtalk.com/)  开发基于钉钉平台相关应用

#### 钉钉开放平台集成方式
- 企业内部应用，供企业内部人员使用
- 第三方企业应用，是指开发者以钉钉、企业之外的第三方身份，基于钉钉的开放能力开发应用，并提供给钉钉上的其他组织使用
- 第三方个人应用，提供给钉钉上的个人用户来使用，不需要企业进行授权开通
- 移动应用接入，Android和IOS的SDK接入


#### 实现功能
- [钉钉成员与企业邮箱联动](https://tower.im/teams/257331/documents/33799/)
- [钉钉成员考评系统](https://tower.im/teams/257331/documents/33879/)


# 小程序免密登录
![dingding](https://raw.githubusercontent.com/ni-ning/lightning/master/images/epsilon/dingding.jpg)

# dingtalk-sdk 源码入门

```
# 安装依赖
pip install dingtalk-sdk[cryptography]

# 输入配置，获取全局client
from dingtalk import AppKeyClient
client = AppKeyClient(config['corp_id'], config['app_key'], config['app_secret'])

# 简单使用
client.user.getuserinfo('userid')
client.department.list()

```


#### 源码的打包、分发、部署
源码文件 `dingtalk-sdk/setup.py`

- 代码编写完毕，`git push` 提交代码，运维人员在生产服务器 `git pull` 源码，启动服务
- 对于开源项目，把源码打包一个文件，上传到 `pypi` 服务器，使用者用 `pip install package` 安装即可

对应文件 `dingtalk-sdk/setup.py`，安装依赖与操作步骤

```
pip install setuptools
pip install wheel
pip install twine
```
- python setup.py bdist_wheel
- 注册 https://pypi.org/
- twine upload dist/*
- 输入username和password上传到pypi


#### 持续集成 CI
源码文件 `dingtalk-sdk/.travis.yml`

编写代码只是软件开发的一小部分，更多的时间往往花在构建 (build) 和测试 (test)

> Travis-CI 是一个开源的持续构建项目，能够测试和部署；Travis-CI 会同步你在 GitHub 上托管的项目，每当你 Commit Push 之后，就会在几分钟内开始按照你的要求测试部署你的项目
> 
> 目前 Travis-CI 分 http://travis-ci.org/ （GitHub 公开项目进这个）和 http://travis-ci.com/ （私有付费项目）
> 
> 官方文档：https://docs.travis-ci.com/



#### 配置文件 YAML
源码文件 `dingtalk-sdk/*.yml`
```YAML
YAML: YAML Ain't Markup Language

PyPI: PyYAML 
```
> 编程免不了要写配置文件，怎么写配置也是一门学问
>
> YAML是专门用来写配置文件的语言，非常简洁和强大，远比JSON格式方便

- [YAML 语言教程](https://www.ruanyifeng.com/blog/2016/07/yaml.html)
- [YAML 官方文档](https://pyyaml.org/wiki/PyYAMLDocumentation)

#### 软件测试 PyTest
源码文件 `dingtalk-sdk/pytest.ini`

`pytest`是一个全功能的测试框架，命令行执行 `pytest -v sample.py`
```
# sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

- [单元测试教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936)
- [PyPI 安装说明](https://pypi.org/project/pytest/)
- [PyTest官方文档](https://www.pytest.org/en/latest/)

#### 软件测试 Tox
源码文件 `dingtalk-sdk/tox.ini`

tox是通用的虚拟环境管理和测试命令行工具
- 不同Python环境下检查依赖包是否正确安装
- 配置测试工具，不同环境下测试代码
- 作为持续集成服务器的前端，大大减少流程化测试所需的时间

```
# content of: tox.ini , put in same dir as setup.py
[tox]
envlist = py27,py37

[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest
commands =
    # NOTE: you can run any command line tool here - not just tests
    pytest
```

- [tox 官文文档](https://tox.readthedocs.io/en/latest/)


#### 标记语言 RST
源码文件 `dingtalk-sdk/*.rst`

reStructuredText 扩展名为.rst是一种轻量级标记语言

Python编程语言的Docutils项目的一部分，Docutils 能够从Python程序中提取注释和信息，格式化成程序文档

- [官方文档](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

#### 文档生成 ReadTheDocs
源码文件 `dingtalk-sdk/.readthedocs.yml`

- [功能说明](https://dingtalk-sdk.readthedocs.io/zh_CN/latest/)
- [官方文档](https://readthedocs.org/)

#### 统一版本 Bumpversion
源码文件 `dingtalk-sdk/.bumpversion`

Bumversion 默认的版本号格式是 {major}.{minor}.{patch}
```
pip install bumpversion

bumpversion major
bumpversion minor
bumpversion path
```

#### 其他文件
- [README.rst](http://docutils.sourceforge.net/rst.html)
- .gitignore
- requirements.txt
- [LICENSE](https://choosealicense.com/) [常用许可证](http://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html)


#### 小试牛刀
- 腾讯企业邮开源项目 [exmail-sdk](https://github.com/ni-ning/exmail-sdk)
