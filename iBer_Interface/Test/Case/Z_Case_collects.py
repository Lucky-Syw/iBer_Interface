# coding=UTF-8

'''
Created on 2019年04月22日

@author: Lucky
用途：集成所有要运行的case，一次执行多条不同case下的不同case条数
'''

import unittest
from Test.Case import login
from Test.Case import Todo

#构造测试集
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(login.C_login))  #因登录接口只需要执行1次，因此放入到循环外

for tmp in range(1):
    '''修改循环数代表着case运行的次数,可对接口做压力测试'''

    #loadTestsFromTestCase只可添加类，因此需要进行如上的赋值操作
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Todo.Todo))
