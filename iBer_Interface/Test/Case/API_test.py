#!/usr/bin/env python
# coding=UTF-8

import unittest
from Test.Module.Todo.Create_todo import todo
from Test.Module.Todo.API_test import API

class Api_Case_Test(unittest.TestCase):
    '''API所测接口集合'''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # def test_02_Create_todo(self):
    #     self.todo = todo()
    #     self.todo.test_create_todo()

    def test_03_get_all_dyn_data(self):
        pass
        '''get-all-dyn-data'''
        # self.api_test = API()
        # # self.todoreport.get_share_code()
        # self.api_test.quan()

    def test_04_un_read_count(self):
        '''un-read-count'''
        self.api_test = API()
        self.api_test.unread()



