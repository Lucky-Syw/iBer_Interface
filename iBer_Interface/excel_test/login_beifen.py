#!/usr/bin/env python
# coding=UTF-8
import requests
from Common import gol
from Common.logs import logging
import yaml,sys,os
from readExcel import ExcelUtil
from writeExcel import Write_excel,copy_excel

# 导入yaml中的host
reload(sys)
sys.setdefaultencoding("utf-8")

root_path = os.getcwd()[:-5]
with open("/Users/lucky/Desktop/Auto/iBer_Python_Interface/iBer_Interface/Config/host_header.yaml", 'rb') as f:
    data = yaml.load(f)
host = data["host"]
get_headers = data["headers"]
logging.info(get_headers)

class login:
    gol._init()

    def __init__(self):
        self.log = logging

    def test_login(self):

        #url = host+"user/login"   #接口
        url = "https://dev1app.goodiber.com/v2/user/login"

        url_Write_excel = url[url.rfind('/v2'):]  # 获取非域名外的url链接，最后写入到Excel中

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

        r = requests.post(url=url, data=data, headers=headers, verify=False,timeout = 3)

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
            version = get_headers["version"]
            version_id = get_headers["version-id"]
        else:
            self.log.error("登录失败")
            raise  False

        self.log.info("请求此接口的响应时间："+str(r.elapsed.total_seconds()))
        self.log.info(r.json())  #打印的reponse返回的所有内容
        self.log.info(requests.get(url))

        res={}
        print ("页面返回的信息：%s"%r.content.decode("utf-8"))
        res["url"] = ""
        res["statuscode"] = str(r.status_code)
        res["times"]  = str(r.elapsed.total_seconds())
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        return res

    def wirte_result(result,filename="testreport.xlsx"):
        # 返回结果的行数row_nub
        row_nub = result['rowNum']
        # 写入statuscode
        wt = Write_excel(filename)
        wt.write(row_nub, 7, result['statuscode'])       # 写入返回状态码statuscode,第8列
        wt.write(row_nub, 8, result['times'])            # 耗时
        wt.write(row_nub, 9, result['error'])            # 状态码非200时的返回信息
        #wt.write(row_nub, 13, result['msg'])           # 抛异常

if __name__ == "__main__":
    data = ExcelUtil("lucky_excel_test.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = login()
    res.test_login()
    copy_excel("lucky_excel_test.xlsx", "testreport.xlsx")
    res.wirte_result(res,filename="testreport.xlsx")

