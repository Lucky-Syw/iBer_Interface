#!/usr/bin/env python
# coding=UTF-8

'''此文件主要是获取cfg.ini中对应的配置信息'''
import os
import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(cur_path,"cfg.ini")
conf = ConfigParser.ConfigParser()
conf.read(configpath)

smtp_server = conf.get("email","smtp_server")

sender = conf.get("email","sender")

psw = conf.get("email","psw")

receiver = conf.get("email","receiver")

port = conf.get("email","port")

'''测试时通过print查看获取的值是否正确，不用释放开'''
# print cur_path
# print configpath
# print smtp_server
# print sender
# print psw
# print receiver
# print port