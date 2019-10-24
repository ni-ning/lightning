# -*-coding:utf-8 -*-
'''
命令行参数解析模块 argparse，即对sys.args进行解析
支持自动生成help命令和帮助文档
'''

import argparse

parse = argparse.ArgumentParser(description='used for test')
args = parse.parse_args()

