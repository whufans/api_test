#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:10
# @Author  : fans
# @File    : test_3_penalty_execution.py
# @Software: PyCharm Community Edition
import time,pytest
from PageObjects.Penalty_Execution import Penalty_Execution_Page
from TestDatas import Penalty_Execution_Datas as PED
@pytest.mark.pe
@pytest.mark.usefixtures("login_prepare_env")
@pytest.mark.usefixtures("refresh_env")
class Test_Penalty_Execution():
	@pytest.mark.parametrize("data",PED.PRISON_EXECUTION_datas)
	def test_first_page_search(self,data,login_prepare_env):
		pe=Penalty_Execution_Page(login_prepare_env)
		pe.enter_penalty_execution_page()
		res =pe.search_firstpage(data["search_text"])
		assert  data["check"]==res

	@pytest.mark.parametrize("data", PED.COMMUNITY_CORRECTION_datas)
	def test_second_page_search(self,data,login_prepare_env):
		pe=Penalty_Execution_Page(login_prepare_env)
		pe.enter_penalty_execution_page()
		pe.enter_seccond_page()
		res =pe.search_secondpage(data["search_text"])
		assert data["check"]==res
