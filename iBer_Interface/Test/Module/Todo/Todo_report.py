#!/usr/bin/env python
# coding=UTF-8

import requests
from Common import gol
from Common.logs import logging
import yaml,sys,os
from requests import exceptions

# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

with open(os.getcwd()[:-5] + "/Config/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]   #获取到url
header = data["headers"]  #获取到host

class share_report:
    def __init__(self):
        self.log = logging

    def get_share_code(self):
        url = host+"todo-report/get-share-code"
        data = {}
        headers = header #获取请求头
        headers.update(uuid=gol.get_value("uuid"), token=gol.get_value("token"))  #yaml中的请求头中未加入uuid和token，因此这里需要加入上去

        #timeout=(0.01,0.1)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=0.5)  # 设置的超时时间为0.5s
        '''判断：根据reponse中的某个值来判断接口返回是否成功'''
        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("获取分享码成功：%s"%(str(r.json()["data"]["share_code"])))
        else:
            self.log.error("获取分享码失败")
            raise False

        self.log.info("请求此接口的响应时间："+str(r.elapsed.total_seconds()))
        self.log.info(r.json())  #打印的reponse返回的所有内容





