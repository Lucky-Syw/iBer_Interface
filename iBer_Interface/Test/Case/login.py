#!/usr/bin/env python
# coding=UTF-8

import unittest
from Test.Module.login.login import login

class C_login(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_login(self):
        '''登录'''
        a = login()
        a.test_login()


