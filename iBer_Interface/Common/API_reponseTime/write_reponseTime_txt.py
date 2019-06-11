#!/usr/bin/env python
# coding=UTF-8

'''用途：将每个接口测试的获取到的url、times写入到txt文件中'''

def write_txt(urls,times):
    path = "/Users/lucky/Desktop/Auto/iBer_Python_Interface/iBer_Interface/Result/"

    with open(path+"API_result.txt","a") as file:
        file.write(urls+" "+times+"\n")