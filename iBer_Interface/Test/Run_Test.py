#!/usr/bin/env python
# coding=UTF-8

import os,time
import unittest
from Common.logs import logging
from Test.Case.Z_Case_collects import suite
import Common.HTMLTestRunner2
from Common.email_L import email_L

class run(unittest.TestCase):

   def test_Runtest(self):
      now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
      File_Path = os.getcwd()[:-5]+ '/Result/Report' + "/"  # 获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
      #print File_Path
      if not os.path.exists(File_Path):
          os.makedirs(File_Path)
      #logging.info(File_Path)
      Report_FileName = file(File_Path + now + r"_API测试报告.html", 'wb')
      runner = Common.HTMLTestRunner2.HTMLTestRunner(stream=Report_FileName, title="接口测试报告",
                                                  description="用例执行情况:",verbosity=2)   #verbosity=2:将会取到方法名下的注释内容

      result = runner.run(suite)  ## suite为Case_Gathers.py中的suite，用法：将case中的suite添加到报告中生成

      Report_FileName.close()

################################如下：测试结果邮件发送给对应接收者，###################################
'''代码调试阶段，可注销此端代码，避免重复发送邮件'''

      # print "运行成功的数目",result.success_count
      # print "运行失败的数目",result.failure_count
      # print "运行测试用例的总数",Common.HTMLTestRunner2.HTMLTestRunner.total

      # time.sleep(2)
      # y = email_L()
      # #y.test_run()    #无论成功失败均发送邮件
      #
      # if result.success_count != Common.HTMLTestRunner2.HTMLTestRunner.total:
      #    y.test_run(status = "FAIL")   #接口用例有执行失败，则发送的邮件标题中会标出【Fail】
      #    logging.error("用例中执行有失败，请查看邮件！！！！")
      # else:
      #    y.test_run(status="PASS")  #与上面反之，标注【Pass】
      #    logging.error("用例执行全部成功，请查看邮件！！！！")


if __name__ == "__main__":
   unittest.main()

