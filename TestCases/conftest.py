#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:15
# @Author  : fans
# @File    : conftest.py
# @Software: PyCharm Community Edition
import pytest,time
from selenium import webdriver
from TestDatas import Common_Datas as CD,login_datas as LD
from PageObjects.LoginPage import LoginPage
driver = None
@pytest.fixture(scope="class")
def  prepare_env():
	global driver
	print("-------测试类级别------------")
	driver = webdriver.Chrome()
	driver.get(CD.url)
	time.sleep(3)
	driver.maximize_window()
	yield  driver
	driver.quit()

@pytest.fixture(scope="class")
def  login_prepare_env():
	global driver
	print("-------测试类级别------------")
	driver = webdriver.Chrome()
	driver.get(CD.url)
	time.sleep(3)
	driver.maximize_window()
	lp = LoginPage(driver)
	lp.login(LD.sfj_account["user"], LD.sfj_account["pwd"])
	yield  driver
	driver.quit()

@pytest.fixture
def  refresh_env():
	global  driver
	print("-------测试用例级别------------")
	yield
	driver.refresh()


