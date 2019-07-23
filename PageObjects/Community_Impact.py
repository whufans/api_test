#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:01
# @Author  : fans
# @File    : Community_Impact.py
# @Software: PyCharm Community Edition
import time
from PageLocators.Community_Impact_Locators import Community_Impact_Locators as cil
from Common.BasePage import BasePage
class Community_Impact_Page(BasePage):
	def  enter_community_impact_page(self):
		self.wait_eleVisible(cil.main_page_xpath)
		self.click_element(cil.main_page_xpath)

	def  search(self,search_text):
		self.wait_eleVisible(cil.search_text_xpath)
		self.input_text(cil.search_text_xpath,search_text)
		time.sleep(0.5)
		# self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(Keys.ENTER)
		self.click_element(cil.search_button_xpath)
		time.sleep(1)
		return  self.get_element_text(cil.search_res_xpath)
