# -*-coding:utf-8 -*-
'''
命令行参数解析模块 argparse，即对sys.args进行解析
支持自动生成help命令和帮助文档
'''

import argparse

parser = argparse.ArgumentParser(description='This script is just used for test.')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s version: 0.0.1', help='show the version')

parser.add_argument('-d', '--debug', action='store_true', default=False,
                    help='show the debug')

args = parser.parse_args()

args = vars(args)
print(args)

