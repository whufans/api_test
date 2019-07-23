#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:51
# @Author  : fans
# @File    : suite&runner.py
# @Software: PyCharm Community Edition
import HTMLTestRunnerNew
import unittest
from Common import constants

discover=unittest.defaultTestLoader.discover(start_dir=constants.TestCases_dir, pattern='test_*.py', top_level_dir=None)
with open(constants.reports_path, 'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='TestReport',description='UI自动化测试报告',tester='范震')
    runner.run(discover)