#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 15:32
# @Author  : fans
# @File    : LoginPage.py
# @Software: PyCharm Community Edition
from PageLocators.Login_Page_Locators import Login_Page_Locators  as lpl
from Common.BasePage import BasePage
class LoginPage(BasePage):
	def login(self,username,passwd):
		self.wait_eleVisible(lpl.login_username_xpath)
		self.clear_ele(lpl.login_username_xpath)
		self.input_text(lpl.login_username_xpath,username)
		self.clear_ele(lpl.login_password_xpath)
		self.input_text(lpl.login_password_xpath,passwd)
		self.click_element(lpl.login_button_xpath)

	def get_login_title(self):
		self.wait_eleVisible(lpl.login_title_xpath)
		return self.get_element_text(lpl.login_title_xpath)

	def get_error_msg(self):
		self.wait_eleVisible(lpl.login_error_msg_xpath)
		return self.get_element_text(lpl.login_error_msg_xpath)
