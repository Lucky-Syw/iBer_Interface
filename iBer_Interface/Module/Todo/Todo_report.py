#!/usr/bin/env python
# coding=UTF-8

import requests
from Common import gol
import yaml,sys,os
from Common.logs import logging

# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

with open(os.getcwd() + "/Configuration/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]   #获取到url
header = data["headers"]  #获取到host

class share_report:
    def __init__(self):
        self.log = logging

    def get_share_code(self):
        url = host+"todo-report/get-share-code"
        data = {}
        headers = header
        headers.update(uuid=gol.get_value("uuid"), token=gol.get_value("token"))  #yaml中的请求头中未加入uuid和token，因此这里需要加入上去

        r = requests.post(url=url, data=data, headers=headers, verify=False)
        self.log.info("获取分享待办code码，如下是reponse返回的内容")
        self.log.info(r.json())