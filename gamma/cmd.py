# -*-coding:utf-8 -*-
'''
命令行参数解析模块 argparse，即对sys.args进行解析
支持自动生成help命令和帮助文档

-h 直接输出帮助文档，无其他流程
-v 直接输出版本信息，无其他流程

-d 则会进入解析流程 args
'''

import argparse

parser = argparse.ArgumentParser(description='This script is just used for test.')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s version: 0.0.1', help='show the version')

# action='store_true'含义解析 默认(即不指定)为False; -d, --debug 则debug=True
parser.add_argument('-d', '--debug', action='store_true', default=False,
                    help='show the debug')

# 用单词做参数，默认为必选参数
parser.add_argument('name')
# 参数类型，可以进行有效约束
parser.add_argument('age', type=int)

# 可选参数 -或--开头
parser.add_argument('-V', '--verbose', help='increase output verbose.')

args = parser.parse_args()
args = vars(args)
print(args)



