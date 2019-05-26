#!/usr/bin/env python
# coding=UTF-8

import unittest
from Module.login.login import login
from Module.Todo.Create_todo import todo
from Module.Todo.Todo_report import share_report
import Common.HTMLTestRunner2
import time,os

class run(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_login(self):
        '''登录'''
        a = login()
        a.test_login()

    # def test_02_Create_todo(self):
    #     self.todo = todo()
    #     self.todo.test_create_todo()

    def test_03_Todo_report(self):
        '''进入计划报告页面'''
        self.todoreport = share_report()
        self.todoreport.get_share_code()

if __name__ == "__main__":
   # unittest.main()
   now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
   File_Path = os.getcwd()+ '/Result/Report' + "/"  # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
   print File_Path
   if not os.path.exists(File_Path):
       os.makedirs(File_Path)
   #logging.info(File_Path)
   Report_FileName = file(File_Path + now + r"_ReportResult.html", 'wb')
   print Report_FileName
   runner = Common.HTMLTestRunner2.HTMLTestRunner(stream=Report_FileName, title="接口测试报告",
                                               description="用例执行情况:",verbosity=2)   #verbosity=2:将会取到方法名下的注释内容
   suite = unittest.TestLoader().loadTestsFromTestCase(run)

   runner.run(suite)  ## suite为Case_Gathers.py中的suite，用法：将case中的suite添加到报告中生成

   Report_FileName.close()

