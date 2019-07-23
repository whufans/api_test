#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:41
# @Author  : fans
# @File    : Login_Page_Locators.py
# @Software: PyCharm Community Edition
class Login_Page_Locators:
	login_title_xpath='//div[@class="el-col el-col-24"]/p'
	login_username_xpath='//div[@class="el-input"]/input[@type="text"]'
	login_password_xpath='//div[@class="el-input"]/input[@type="password"]'
	login_button_xpath='//div[@class="el-row"]'
	login_error_msg_xpath='//p[@class="error"]'