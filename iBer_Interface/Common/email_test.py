#!/usr/bin/env python
# coding=UTF-8

import os,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Common.logs import logging
from Config.email import readConfig

report_path = os.getcwd()[:-7] + '/Result/Report' + "/"
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

sender = "lucky@iberhk.com"
psw = "A1q2w3e4r"
receiver = '904199561@qq.com'
smtp_server = "smtp.exmail.qq.com"
Port = "465"

class email_L:

    def get_Report_file(self,report_path):
       '''
        用途：获取最新的API测试报告
        参数介绍：
            report_path：报告存储的路径
       '''
       logging.info("获取最新的测试报告")
       lists = os.listdir(report_path)
       #print lists
       lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
       logging.info(u"最新测试生成的报告：" + lists[-1])
       report_file = os.path.join(report_path, lists[-1])
       return report_file

    def send_mail(self,sender, psw, receiver, smtpserver, report_file, port,status):
       '''
       用途：发送最新的测试报告
       参数介绍：
            sender：发送者
            psw：QQ的授权码
            receive：接收者
            smtpserver：邮件的格式
            report_file：发送的邮件附件
            port：邮箱的端口
       '''
       logging.info("邮件发送最新的API测试报告")
       with open(report_file, "rb") as f:
          mail_body = f.read()

       # 定义邮件内容
       msg = MIMEMultipart()
       body = MIMEText(mail_body, _subtype="html", _charset="utf-8")
       msg['subject'] = u"【%s】iBer接口自动化测试报告"%status
       msg['from'] = sender
       msg['to'] = psw
       msg.attach(body)

       # 添加附件
       att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
       att["Content-Type"] = "application/octet-stream"
       att["Content-Disposition"] = 'attachment;filename = "report.html"'
       msg.attach(att)
       try:
          smtp = smtplib.SMTP_SSL(smtpserver, port)
       except:
          smtp = smtplib.SMTP()
          smtp.connect(smtpserver, port)

       # 用户名和密码
       smtp.login(sender, psw)
       smtp.sendmail(sender, receiver, msg.as_string())
       smtp.quit()
       logging.info("API测试报告已发送成功 !")
       receiver = readConfig.receiver
       logging.info("已发送的邮箱： %s" %receiver)

    def test_run(self,status):
        '''如上2个方法的集合整理方法'''

        report_file = self.get_Report_file(report_path)
        # 邮箱配置
        # sender = readConfig.sender
        # psw = readConfig.psw
        # smtp_server = readConfig.smtp_server
        # port = readConfig.port
        # receiver = readConfig.receiver
        self.send_mail(sender, psw, receiver.split(','), smtp_server, report_file, Port,status)  # 发送报告

if __name__ == "__main__":
    a = email_L()
    a.test_run("PASS")