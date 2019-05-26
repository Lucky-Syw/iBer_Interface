#!/usr/bin/env python
# coding=UTF-8

import unittest
from Test.Module.Todo.Create_todo import todo
from Test.Module.Todo.Todo_report import share_report

class Todo(unittest.TestCase):
    '''行动计划'''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # def test_02_Create_todo(self):
    #     self.todo = todo()
    #     self.todo.test_create_todo()

    def test_03_Todo_report(self):
        '''进入计划报告页面'''
        self.todoreport = share_report()
        self.todoreport.get_share_code()