#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:05
# @Author  : fans
# @File    : test_2_community_impact.py
# @Software: PyCharm Community Edition
import time,pytest
from PageObjects.Community_Impact import Community_Impact_Page
from TestDatas import Community_Impact_Datas as CID
@pytest.mark.ci
@pytest.mark.usefixtures("login_prepare_env")
@pytest.mark.usefixtures("refresh_env")
class Test_Community_Impact():
	@pytest.mark.parametrize("data",CID.search_datas)
	def test_search(self,data,login_prepare_env):
		ci=Community_Impact_Page(login_prepare_env)
		ci.enter_community_impact_page()
		res =ci.search(data["search_text"])
		assert data["check"]==res