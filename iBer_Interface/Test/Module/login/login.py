#!/usr/bin/env python
# coding=UTF-8
import requests
from Common import gol
from Common.logs import logging
import yaml,sys,os

# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

root_path = os.getcwd()[:-5]
with open(root_path + "/Configuration/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]

class login:
    gol._init()

    def __init__(self):
        self.log = logging

    def test_login(self):

        url = host+"user/login"   #接口

        data = {
            "mobile": "12606666333",
            "password": "33a7d3da476a32ac237b3f603a1be62fad00299e0d4b5a8db8d913104edec629"
        }
        headers = {
            "version": "2.3.0",
            "version-id": "235",
            "device-id": "8BAFD18C-61E3-4BAF-8AB1-0BC16E567633",
            "time": "1557728866628",
            "channel-id": "001",
            "os": "ios",
            "Accept-Language": "zh-tw",
            "device-name": "iPhoneX",
            "User-Agent": "iBer/235 CFNetwork/976 Darwin/18.2.0",
            #注：一定不能加content-type，否则报签名错误
            # Content-Type: multipart/form-data; boundary=vHsPJ5s6grMzpmWoZxd3T3o6.LcUWBvUUu0gDNubaf05Ve7kv6bAkH3s_rr0AEc2D6AbEh
            "sign": "a81b4379f504f330e83792ce2015e629"
        }

        r = requests.post(url=url, data=data, headers=headers, verify=False)
        uuid = str(r.json()["data"]["uuid"])
        gol.set_value("uuid", uuid)
        token = str(r.json()["data"]["token"])
        gol.set_value("token", token)
        version = "2.2.1"
        version_id = "232"

        self.log.info("登录成功，如下是reponse返回的内容")
        self.log.info(r.text)


