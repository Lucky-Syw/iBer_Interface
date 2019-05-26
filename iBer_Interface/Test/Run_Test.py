#!/usr/bin/env python
# coding=UTF-8

import unittest
import Common.HTMLTestRunner2
import time,os
from Test.Case.Z_Case_collects import suite


class run(unittest.TestCase):

   now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
   File_Path = os.getcwd()[:-5]+ '/Result/Report' + "/"  # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
   print File_Path
   if not os.path.exists(File_Path):
       os.makedirs(File_Path)
   #logging.info(File_Path)
   Report_FileName = file(File_Path + now + r"_ReportResult.html", 'wb')
   print Report_FileName
   runner = Common.HTMLTestRunner2.HTMLTestRunner(stream=Report_FileName, title="接口测试报告",
                                               description="用例执行情况:",verbosity=2)   #verbosity=2:将会取到方法名下的注释内容

   runner.run(suite)  ## suite为Case_Gathers.py中的suite，用法：将case中的suite添加到报告中生成

   Report_FileName.close()

