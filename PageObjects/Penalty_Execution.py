#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:20
# @Author  : fans
# @File    : Penalty_Execution.py
# @Software: PyCharm Community Edition
import time
from PageLocators.Penalty_Execution_Locators import Penalty_Execution_Locators as pel
from Common.BasePage import BasePage
class Penalty_Execution_Page(BasePage):
	def  enter_penalty_execution_page(self):
		self.wait_eleVisible(pel.main_page_xpath)
		self.click_element(pel.main_page_xpath)

	def  enter_first_page(self):
		self.wait_eleVisible(pel.first_page_xpath)
		self.click_element(pel.first_page_xpath)

	def enter_seccond_page(self):
		self.wait_eleVisible(pel.second_page_xpath)
		self.click_element(pel.second_page_xpath)

	def  search_firstpage(self,search_text):
		self.wait_eleVisible(pel.search_text_xpath1)
		self.input_text(pel.search_text_xpath1,search_text)
		time.sleep(0.5)
		# self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(Keys.ENTER)
		self.click_element(pel.search_button_xpath1)
		time.sleep(1)
		return   self.get_element_text(pel.search_res_xpath1)

	def  search_secondpage(self,search_text):
		self.wait_eleVisible(pel.search_text_xpath2)
		self.input_text(pel.search_text_xpath2, search_text)
		time.sleep(0.5)
		# self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(Keys.ENTER)
		self.click_element(pel.search_button_xpath2)
		time.sleep(1)
		return self.get_element_text(pel.search_res_xpath2)
