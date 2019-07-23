#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:44
# @Author  : fans
# @File    : Community_Impact_Locators.py
# @Software: PyCharm Community Edition
class Community_Impact_Locators:
	#社区影响评估菜单
	main_page_xpath = '//a[text()="社区影响评估"]'
	#搜索文本框
	search_text_xpath = '//input[@placeholder="被告人姓名/证件号"]'
	#搜索结果条数
	search_res_xpath = '//span[@class="el-pagination__total"]'
	#搜索按钮
	search_button_xpath = '//div[@class="el-input-group__append"]'