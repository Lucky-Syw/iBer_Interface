#!/usr/bin/env python
# coding=UTF-8
import requests
from Common import gol
from Common.logs import logging
import yaml,sys,os
import json


# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

root_path = os.getcwd()[:-5]
with open(root_path + "/Config/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]
timeout = data["timeout"]

class login:
    gol._init()

    def __init__(self):
        self.log = logging

    def test_login(self):
        url = host+"user/login"   #接口

        url_Write_excel = url[url.rfind('/v2'):]  #获取非域名外的url链接，最后写入到Excel中

        #"password": "33a7d3da476a32ac237b3f603a1be62fad00299e0d4b5a8db8d913104edec629"   22222222的密码，下方写的是11111111的密码
        data = {
            "mobile": "12606666333",
            "password": "ee79976c9380d5e337fc1c095ece8c8f22f91f306ceeb161fa51fecede2c4ba1"
        }
        headers = {
            "version": "2.3.1",
            "version-id": "239",
            "device-id": "6B33C356-CB5F-4F51-B503-36ABA6AD0B02",
            "time": "1560175716224",
            "channel-id": "001",
            "os": "ios",
            "Accept-Language": "zh-tw",
            "device-name": "iPhoneX",
            "User-Agent": "iBer/239 CFNetwork/902.2 Darwin/17.7.0",
            #注：一定不能加content-type，否则报签名错误
            # Content-Type: multipart/form-data; boundary=vHsPJ5s6grMzpmWoZxd3T3o6.LcUWBvUUu0gDNubaf05Ve7kv6bAkH3s_rr0AEc2D6AbEh
            "sign": "629bb0721dc60ff71725b40f46a3d1b5"
        }

        r = requests.post(url=url, data=data, headers=headers, verify=False,timeout = timeout)
        get_reponse = r.json() # 获取到reponse返回的所有内容
        result = json.dumps(get_reponse, encoding="utf-8", ensure_ascii=False)   #将获取到的reponse中的中文已utf-8的格式显示。否则显示Unicode

        self.log.info(result)
        '''
        判断：
        1、根据reponse中的某个值来判断接口返回是否成功，
        2、成功的情况下，再次去获取uuid等值。
        '''

        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("登录成功")
            uuid = str(r.json()["data"]["uuid"])
            gol.set_value("uuid", uuid)
            token = str(r.json()["data"]["token"])
            gol.set_value("token", token)
            # version = get_headers["version"]
            # version_id = get_headers["version-id"]
        else:
            self.log.error("登录失败")
            raise  False

        self.log.info("请求此接口的响应时间："+str(r.elapsed.total_seconds()))
        # self.log.info(r.json())  #打印的reponse返回的所有内容
        self.log.info(str(url_Write_excel)+"########")



        ########################获取URL和times(超时时间)数据的写入txt文件#########################
        from Common.API_reponseTime.write_reponseTime_txt import write_txt

        urls = url_Write_excel    #获取的url
        times = str(r.elapsed.total_seconds())   # 获取到响应时间temeout
        write_txt(urls,times)