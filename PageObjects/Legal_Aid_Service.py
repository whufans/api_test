#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:39
# @Author  : fans
# @File    : Legal_Aid_Service.py
# @Software: PyCharm Community Edition
import os,time
from PageLocators.Legal_Aid_Service_Locators import Legal_Aid_Service_Locators as lasl
from Common.BasePage import BasePage
class Legal_Aid_Service_Page(BasePage):
	#点击法律援助服务模块
	def  enter_legal_aid_service_page(self):
		self.wait_eleVisible(lasl.main_page_xpath)
		self.click_element(lasl.main_page_xpath)

	#搜索
	def  search(self,search_text):
		self.wait_eleVisible(lasl.search_text_xpath)
		self.input_text(lasl.search_text_xpath,search_text)
		time.sleep(0.5)
		# self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(Keys.ENTER)
		self.click_element(lasl.search_button_xpath)
		time.sleep(1)
		return  self.get_element_text(lasl.search_res_xpath)

	#翻页功能-1向前翻页  0向后翻页   >0的数字 翻到指定页码
	def  page_handle(self,pageId=0):
		if pageId==-1:
			self.click_element(lasl.button_prev)
		elif pageId==0:
			self.click_element(lasl.button_next)
		else :
			if  pageId>0:
				self.click_element('// li[text() = {}]'.format(pageId))
		time.sleep(2)

	#已受理1  已反馈 2    已终止3
	def detail(self,index=1):
		time.sleep(2)
		if index==1:
			while(not self.page_should_contain_element(lasl.sl_button)):
				self.page_handle(0)
			self.click_element(lasl.sl_button)
		elif index==2:
			while (not self.page_should_contain_element(lasl.fh_button)):
				self.page_handle(0)
			self.click_element(lasl.fh_button)
		elif index==3:
			while (not self.page_should_contain_element(lasl.zz_button)):
				self.page_handle(0)
			self.click_element(lasl.zz_button)

	#回到案件列表
	def back_to_case_list(self):
		self.click_element(lasl.case_list)
		time.sleep(1)

	#上传文件
	def  upload_file(self):
		self.click_element(lasl.upload_button)
		os.system("C:\\Users\\admin\\PycharmProjects\\Practice\\uploadfile1.exe")
		time.sleep(6)

	#填写法律援助服务内容
	def  input_legal_aida(self,text1,text2,text3,text4,text5):
		self.input_text(lasl.input1,text1)
		self.input_text(lasl.input2,text2)
		self.input_text(lasl.input3,text3)
		self.input_text(lasl.input4,text4)
		self.input_text(lasl.input5,text5)

	#提交
	def submit(self):
		self.click_element(lasl.submit)
		time.sleep(5)

	#终止
	def  end(self,text):
		self.click_element(lasl.end_button)
		self.input_text(lasl.end_textarea,text)
		self.click_element(lasl.confirm_end_button)
		time.sleep(5)

	#获取状态
	def case_status(self):
		time.sleep(2)
		return  self.get_element_text(lasl.case_status)

