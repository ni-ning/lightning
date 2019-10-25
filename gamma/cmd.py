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
parser.add_argument('name', help='test positional argument')
# 参数类型，可以进行有效约束
parser.add_argument('age', type=int, help='test argument type')

# 可选参数 -或--开头
parser.add_argument('-V', '--verbose', help='increase output verbose.')

# 有些参数，是互斥的，有你无我，如性别
# 实际测试情况，都不填时，默认都是False
group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--male', action='store_true', help='test group argument')
group.add_argument('-f', '--female', action='store_true', help='test group argument')
# 可选列表值，是较好的实践
parser.add_argument('-g', '--gender', default='male',
                    choices=['male', 'female'], help='test choices list')

# 多余的位置参数
parser.add_argument('options', default=[], nargs='*')

args = parser.parse_args()
args = vars(args)
print(args)



