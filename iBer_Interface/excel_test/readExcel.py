#!/usr/bin/env python
# coding=UTF-8
import xlrd

class ExcelUtil:
    def __init__(self,excelpath,sheetname = "Sheet1"):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.cloNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <=1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum -1)):
                s ={}
                s["rownum"] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.cloNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j +=1
            return r

if __name__ == "__main__":
    filepath = "lucky_excel_test.xlsx"
    sheetname = "Sheet1"
    data = ExcelUtil(filepath,sheetname)
    print(data.dict_data())











































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
