#!/usr/bin/env python
# coding=UTF-8

'''此文件主要是获取cfg.ini中对应的配置信息'''
import os
import ConfigParser


cur_path = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(cur_path,"cfg.ini")
conf = ConfigParser.ConfigParser()
conf.read(configpath)

'''获取到email的相关信息'''
smtp_server = conf.get("email","smtp_server")
sender = conf.get("email","sender")
psw = conf.get("email","psw")
receiver = conf.get("email","receiver")
port = conf.get("email","port")

'''获取到mysql的相关信息'''

host = conf.get("Test_Env_mysql","host")
user = conf.get("Test_Env_mysql","user")
passwd = conf.get("Test_Env_mysql","passwd")
db = conf.get("Test_Env_mysql","db")