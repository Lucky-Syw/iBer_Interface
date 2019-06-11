#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:lucky,time:2019-06-11

import pymysql,sys
import readConfig
import json
#连接数据库
db = pymysql.connect(host=readConfig.host,user = readConfig.user,passwd=readConfig.passwd,db=readConfig.db) #db：库名
#创建游标
# cur = db.cursor()

#创建游标,结果将已字典的形式返回
cur = db.cursor(pymysql.cursors.DictCursor)

# sql = "select bs.uuid,bs.target_type,bs.source,bs.user_uuid,bs.agent_uuid from `behavior_share` bs join user u on u.uuid = bs.user_uuid where u.mobile = '12606666333'"
#查询lcj表中存在的数据
sql = "select bs.uuid,bs.agent_uuid from `behavior_share` bs join user u on u.uuid = bs.user_uuid where u.mobile = '12606666333'"

cur.execute(sql)
# #fetchall:获取lcj表中所有的数据
# ret1 = cur.fetchall()
# print(ret1)    #获取所有的查询结果，此处的类型是列表
# print len(ret1)     #获取所有结果的条数
# print ret1[0]        #获取所得结果为0下标的字典
# print type(ret1[0])   #此处的类型是字典
# print ret1[0]["uuid"]   #获取所得结果为0下标的字典中的某个值

print cur.fetchmany(1)   #获取查询结果的前一行的数据
print cur.fetchmany(2)   #获取查询结果的前二行的数据

cur.close()
db.close()



