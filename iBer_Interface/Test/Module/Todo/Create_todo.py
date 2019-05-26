#!/usr/bin/env python
# coding=UTF-8
import requests
from Common import gol
import yaml,sys,os
from Common.logs import logging

# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

with open(os.getcwd()[:-5] + "/Configuration/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]   #获取到url
header = data["headers"]  #获取到host

class todo:

    def __init__(self):
        self.log = logging


    def test_create_todo(self):
        url = host+"todo/create"
        data = {
            "name": "1239",
            "todo_remind_type": "0",
            "cate_uuid": "86799e50d9890ade579c4ac88059a5ff",
            "all_day": "1",
            "todo_start": "2019-05-13",
            "todo_end": "",
            "type": "0",
            "repeat_tyep": "0",
            "c_user_uuid": ""
        }
        headers = header
        headers.update(uuid=gol.get_value("uuid"),token=gol.get_value("token"))
        r = requests.post(url=url, data=data, headers=headers, verify=False)
        self.log.info("创建待办成功，如下是reponse返回的内容")
        self.log.info(r.json())


