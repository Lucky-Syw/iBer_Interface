#!/usr/bin/env python
# coding=UTF-8
import os

report_path = os.getcwd()[:-5]+ '/Result/Report' + "/"
def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir()












































#
# from sshtunnel import SSHTunnelForwarder
# import paramiko
# import  pymysql
#
#
# # 获取密钥
# private_key = paramiko.RSAKey.from_private_key_file('/Users/lucky/Desktop/mysql_C/prod08.28.pem')
# with SSHTunnelForwarder(
#     # 指定ssh登录的跳转机的address
#     ssh_address_or_host = ('120.78.175.201',50008),
#     # 设置密钥
#     ssh_pkey = private_key,
#     # 如果是通过密码访问，可以把下面注释打开，将密钥注释即可。
#     # ssh_password = "password",
#     # 设置用户
#     ssh_username = 'iber',
#     # 设置数据库服务地址及端口
#     remote_bind_address= ('rm-wz94zg82ebbpi665czo.mysql.rds.aliyuncs.com',3306)) as server:
#
#     conn = pymysql.connect(database='rm-wz94zg82ebbpi665czo.mysql.rds.aliyuncs.com',
#                             user='iber_php',
#                             password='cLz1xV07KrQUzCDxVU5kNRedP7lRDRQy',
#                             host='120.0.0.1',  # 因为上面没有设置 local_bind_address,所以这里必须是127.0.0.1,如果设置了，取设置的值就行了。
#                             port=server.local_bind_port) # 这里端口也一样，上面的server可以设置，没设置取这个就行了
#
#
#     print(conn)
#
#     cur = conn.cursor()
#     # 执行查询，查看结果，验证数据库是否链接成功。
#     cur.execute("select * from user where mobile = '12606666333'")
#
#     data = cur.fetchall()
#     print(data)
#     conn.close()
#     cur.close()
