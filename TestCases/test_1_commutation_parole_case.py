#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 19:44
# @Author  : fans
# @File    : test_1_commutation_parole_case.py
# @Software: PyCharm Community Edition
import time,pytest,os
from TestDatas import Common_Datas as CD, login_datas  as LD, Commutation_Parole_Datas as CPD
from PageObjects.Commutation_Parole_Case_Page import Commutation_Parole_Case_Page
from PageObjects.LoginPage import LoginPage
@pytest.mark.cpc
@pytest.mark.usefixtures("login_prepare_env")
@pytest.mark.usefixtures("refresh_env")
class Test_Commutation_Parole_Case():
	@pytest.mark.smoke
	@pytest.mark.parametrize("data",CPD.search_datas)
	def test_search(self,data,login_prepare_env):
		cpcp=Commutation_Parole_Case_Page(login_prepare_env)
		res =cpcp.search(data["search_text"])
		assert data["check"]==res

	def test_upload(self,login_prepare_env):
		cpcp = Commutation_Parole_Case_Page(login_prepare_env)
		res = cpcp.search("UI测试CaseID0301")
		cpcp.upload_file("D:\\PDF.pdf",2)
		# os.system("C:\\Users\\admin\\PycharmProjects\\Practice\\uploadfile1.exe")
		tip=cpcp.get_upload_tip()
		assert   "上传成功！"==tip

	def test_choose_reset(self,login_prepare_env):
		cpcp = Commutation_Parole_Case_Page(login_prepare_env)
		time.sleep(1)
		cpcp.choose()
		res=cpcp.get_first_row_search_result()
		print(res)
		cpcp.reset()
		res = cpcp.get_first_row_search_result()
		print(res)
		assert  "共 32 条"==res

	@pytest.mark.smoke
	def  test_page(self,login_prepare_env):
		cpcp = Commutation_Parole_Case_Page(login_prepare_env)
		cpcp.page_handle(0)
		# num=cpcp.get_page_number()
		# self.assertEqual("2", num)
		cpcp.page_handle(-1)
		# num = cpcp.get_page_number()
		# self.assertEqual("1", num)
		cpcp.page_handle(4)
		# num = cpcp.get_page_number()
		# self.assertEqual("4", num)
		cpcp.jump_page(2)
		# num = cpcp.get_page_number()
		# self.assertEqual("2", num)

	@pytest.mark.smoke
	def test_log_in_upload(self, login_prepare_env):
		cpcp = Commutation_Parole_Case_Page(login_prepare_env)
		res = cpcp.search("UI测试CaseID0301")
		cpcp.log_in_upload()

	@pytest.mark.smoke
	def  test_log_out(self,login_prepare_env):
		cpcp = Commutation_Parole_Case_Page(login_prepare_env)
		cpcp.log_out()
		lp = LoginPage(login_prepare_env)
		title=lp.get_login_title()
		assert CPD.logout_check==title






