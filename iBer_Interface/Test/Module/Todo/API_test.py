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
host = data["host"]    #获取到url
header = data["headers"]     #获取到host


class API:
    def __init__(self):
        self.log = logging

    def get_share_code(self):
        url = host+"todo-report/get-share-code"
        url_Write_excel = url[url.rfind('/v2'):]  # 获取非域名外的url链接，最后写入到Excel中

        data = {}
        headers = header #获取请求头
        headers.update(uuid=gol.get_value("uuid"), token=gol.get_value("token"))  #yaml中的请求头中未加入uuid和token，因此这里需要加入上去

        #timeout=(0.01,0.1)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=15)  # 设置的超时时间为0.5s
        '''判断：根据reponse中的某个值来判断接口返回是否成功'''
        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("获取分享码成功：%s"%(str(r.json()["data"]["share_code"])))
        else:
            self.log.error("获取分享码失败")
            raise False

        self.log.info("请求此接口的响应时间："+str(r.elapsed.total_seconds()))
        self.log.info(r.json())  #打印的reponse返回的所有内容

        ########################获取URL和times(超时时间)数据的写入txt文件#########################
        from Common.API_reponseTime.write_reponseTime_txt import write_txt
        urls = url_Write_excel  # 获取的url
        times = str(r.elapsed.total_seconds())  # 获取到响应时间temeout
        write_txt(urls, times)

    def quan(self):
        '''获取圈子的全部动态'''

        url = host + "c-user-action-log/get-all-dyn-data"
        jiekou = "c-user-action-log/get-all-dyn-data"
        #url_Write_excel = url[url.rfind('/v2'):]  # 获取非域名外的url链接，最后写入到Excel中

        data = {
            "anonymous": "1",
            "degree": "0",
            "cate": "",
            "from": "",
            "page": "3",
            "pagesize": "",
            "customer": "",
            "guestbook": "",
        }
        headers = header  # 获取请求头
        # headers ={
        #     "version": "2.3.0",
        #     "version-id": "235",
        #     "os": "ios",
        #     "sign": "123456",
        #     "is-test": "1",
        #     "uuid": "aece8130e9049a2c21bd585b53dc042a",
        #     "token":"1234"
        #
        # }
        #headers.update(uuid=gol.get_value("uuid"), token=gol.get_value("token"))  # yaml中的请求头中未加入uuid和token，因此这里需要加入上去

        # timeout=(0.01,0.1)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=100000)  # 设置的超时时间为0.5s
        '''判断：根据reponse中的某个值来判断接口返回是否成功'''
        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("获取分享码成功")
        else:
            self.log.error("获取分享码失败")
            #raise False

        self.log.info("请求此接口的响应时间：" + str(r.elapsed.total_seconds()))
        self.log.info(r.json())  # 打印的reponse返回的所有内容

        ########################获取URL和times(超时时间)数据的写入txt文件#########################
        from Common.API_reponseTime.write_reponseTime_txt import write_txt
        urls = jiekou  # 获取的url
        times = str(r.elapsed.total_seconds())  # 获取到响应时间temeout
        write_txt(urls, times)

    def unread(self):
        url = host + "agent-article/reprint"
        jiekou = "agent-article/reprint"
        # url_Write_excel = url[url.rfind('/v2'):]  # 获取非域名外的url链接，最后写入到Excel中

        data =  {"url":"https://mp.weixin.qq.com/s/pmdYAUCHj5QdogvKlIVp0g"}
        headers = header  # 获取请求头
        # headers.update(uuid=gol.get_value("uuid"), token=gol.get_value("token"))  # yaml中的请求头中未加入uuid和token，因此这里需要加入上去

        # timeout=(0.01,0.1)
        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=100000)  # 设置的超时时间为0.5s
        '''判断：根据reponse中的某个值来判断接口返回是否成功'''
        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("获取分享码成功")
        else:
            self.log.error("获取分享码失败")
            # raise False

        self.log.info("请求此接口的响应时间：" + str(r.elapsed.total_seconds()))
        self.log.info(r.json())  # 打印的reponse返回的所有内容

        ########################获取URL和times(超时时间)数据的写入txt文件#########################
        from Common.API_reponseTime.write_reponseTime_txt import write_txt
        urls = jiekou  # 获取的url
        times = str(r.elapsed.total_seconds())  # 获取到响应时间temeout
        write_txt(urls, times)

    def unread2(self):
        url = host + "agent-article/reprint"
        jiekou = "agent-article/reprint"
        # url_Write_excel = url[url.rfind('/v2'):]  # 获取非域名外的url链接，最后写入到Excel中

        data = {"url":"https://mp.weixin.qq.com/s/pmdYAUCHj5QdogvKlIVp0g"}
        headers = header  # 获取请求头

        r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=100000)  # 设置的超时时间为0.5s
        '''判断：根据reponse中的某个值来判断接口返回是否成功'''
        if str(r.json()["msg"]) == "SUCCESS":
            self.log.info("获取分享码成功")
        else:
            self.log.error("获取分享码失败")
            # raise False

        self.log.info("请求此接口的响应时间：" + str(r.elapsed.total_seconds()))
        self.log.info(r.json())  # 打印的reponse返回的所有内容

        ########################获取URL和times(超时时间)数据的写入txt文件#########################
        from Common.API_reponseTime.write_reponseTime_txt import write_txt
        urls = jiekou  # 获取的url
        times = str(r.elapsed.total_seconds())  # 获取到响应时间temeout
        write_txt(urls, times)


