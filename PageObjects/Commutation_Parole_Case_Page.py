#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:09
# @Author  : fans
# @File    : Commutation_Parole_Case_Page.py
# @Software: PyCharm Community Edition
import time
from PageLocators.Commutation_Parole_Case_Locators import Commutation_Parole_Case_Locators as cpcl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Common.BasePage import BasePage
class Commutation_Parole_Case_Page(BasePage):
	def create_case(self):
		self.wait_eleVisible(cpcl.create_case_button_xpath)
		self.click_element(cpcl.create_case_button_xpath)
		pass

	def search(self,search_text):
		self.wait_eleVisible(cpcl.search_text_xpath)
		self.input_text(cpcl.search_text_xpath,search_text)
		time.sleep(0.5)
		# self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(Keys.ENTER)
		self.click_element(cpcl.search_button_xpath)
		time.sleep(1)
		return    self.get_element_text(cpcl.search_res_xpath)

	def  get_first_row_search_result(self):
		# WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.search_res_xpath)))
		time.sleep(1)
		return   self.get_element_text(cpcl.search_res_xpath)

	def log_out(self):
		self.wait_eleVisible(cpcl.user_xpath)
		self.click_element(cpcl.user_xpath)
		self.wait_eleVisible(cpcl.log_out_button)
		self.click_element(cpcl.log_out_button)
		self.wait_eleVisible(cpcl.confirm_button)
		self.click_element(cpcl.confirm_button)

	def get_user_name(self):
		self.wait_eleVisible(cpcl.user_name_xpath)
		return  self.get_element_text(cpcl.user_name_xpath)

	def choose(self,start="2019-03-01",end="2019-03-31",text="盗窃"):
		js= """
                    var dates=document.getElementsByClassName("el-range-input"); 
                    dates[0].value="2019-03-01";
                    dates[1].value="2019-03-31";
                    """
		self.driver.execute_script(js)
		self.input_text(cpcl.case_type,text)
		self.click_element(cpcl.case_type1)
		time.sleep(4)
		self.click_element(cpcl.choose_button)
		time.sleep(2)

	def reset(self):
		self.click_element(cpcl.reset_button)
		time.sleep(2)

	#案件列表上传文件
	def upload_file(self,file,times=1):
		# ele = self.driver.find_element_by_xpath(cpcl.upload_button)
		# ActionChains(self.driver).move_to_element(ele).click().perform()
		self.click_element(cpcl.upload_button)
		if times !=1:
			self.click_element(cpcl.upload_confirm_button)
		time.sleep(2)
		self.upload(file)

	#上传文件提示
	def get_upload_tip(self):
		self.wait_eleVisible(cpcl.upload_tip)
		return self.get_element_text(cpcl.upload_tip)

	#进入证据录入页面
	def log_in_upload(self):
		# ele=self.find_element(cpcl.caseline)
		ele=self.driver.find_element_by_xpath(cpcl.caseline)
		ActionChains(self.driver).move_to_element(ele).click().perform()
		# self.click_element(cpcl.caseId)
		# self.script('$(arguments[0]).click();', ele)

	def  page_handle(self,pageId=0):
		if pageId==-1:
			self.click_element(cpcl.button_prev)
		elif pageId==0:
			self.click_element(cpcl.button_next)
		else :
			if  pageId>0:
				self.click_element('// li[text() = {}]'.format(pageId))
		time.sleep(2)

	def  jump_page(self,pageId):
		self.clear_ele(cpcl.jump_button)
		text=(pageId,Keys.ENTER)
		self.input_text(cpcl.jump_button,*text)
		time.sleep(2)

	def  get_page_number(self):
		time.sleep(2)
		return self.get_element_text(cpcl.jump_button)





