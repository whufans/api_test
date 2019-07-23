#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 13:34
# @Author  : fans
# @File    : test_0_login1.py
# @Software: PyCharm Community Edition
import time,os,pytest
from TestDatas import Common_Datas as CD,login_datas as LD
from PageObjects.Commutation_Parole_Case_Page import Commutation_Parole_Case_Page
from PageObjects.LoginPage import LoginPage
@pytest.mark.login
@pytest.mark.usefixtures("prepare_env")
@pytest.mark.usefixtures("refresh_env")
class Test_Login():
	@pytest.mark.parametrize("data",LD.wrong_datas)
	def test_login_fail(self,prepare_env,data):
		lp = LoginPage(prepare_env)
		lp.login(data["user"], data["pwd"])
		assert  data["check"]==lp.get_error_msg()

	@pytest.mark.smoke
	def test_login_suc(self, prepare_env):
		lp = LoginPage(prepare_env)
		lp.login(LD.sfj_account["user"], LD.sfj_account["pwd"])
		cpc = Commutation_Parole_Case_Page(prepare_env)
		assert cpc.get_user_name() == '司法局测试时'