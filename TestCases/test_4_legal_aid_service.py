#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:41
# @Author  : fans
# @File    : test_4_legal_aid_service.py
# @Software: PyCharm Community Edition
import time,pytest
from TestDatas import  Legal_Aid_Service_Datas as LASD
from PageObjects.Legal_Aid_Service import Legal_Aid_Service_Page
@pytest.mark.las
@pytest.mark.usefixtures("login_prepare_env")
@pytest.mark.usefixtures("refresh_env")
class Test_Legal_Aid_Service():
	@pytest.mark.parametrize("data", LASD.search_datas)
	def test_search(self,data,login_prepare_env):
		self.las = Legal_Aid_Service_Page(login_prepare_env)
		self.las.enter_legal_aid_service_page()
		res =self.las.search(data["search_text"])
		assert   data["check"]==res

	def  test_page(self,login_prepare_env):
		self.las = Legal_Aid_Service_Page(login_prepare_env)
		self.las.enter_legal_aid_service_page()
		self.las.page_handle(0)
		self.las.page_handle(-1)
		self.las.page_handle(4)

	def test_in_and_out(self,login_prepare_env):
		self.las = Legal_Aid_Service_Page(login_prepare_env)
		self.las.enter_legal_aid_service_page()
		self.las.detail(1)
		res = self.las.case_status()
		assert  "(已受理 )" == res
		self.las.back_to_case_list()

	def test_all(self,login_prepare_env):
		self.las = Legal_Aid_Service_Page(login_prepare_env)
		self.las.enter_legal_aid_service_page()
		self.las.detail(1)
		self.las.upload_file()
		self.las.input_legal_aida(*LASD.legal_aid_text)
		self.las.submit()
		res = self.las.case_status()
		assert "(已反馈 )" == res
		self.las.end(LASD.end_reason)
		res=self.las.case_status()
		assert "(已终止\n)" == res




