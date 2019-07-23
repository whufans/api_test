#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:44
# @Author  : fans
# @File    : Penalty_Execution_Locators.py
# @Software: PyCharm Community Edition
class Penalty_Execution_Locators:
	#刑罚交付执行菜单
	main_page_xpath = '//a[text()="刑罚交付执行"]'
	#监禁刑交付执行
	first_page_xpath = '//div[@id="tab-first"]'
	# 监禁刑交付执行搜索文本框
	search_text_xpath1 = '//input[@placeholder="被执行人姓名/证件号"]'
	# 监禁刑交付执行搜索结果条数
	search_res_xpath1 = '//span[@class="el-pagination__total"]'
	# 监禁刑交付执行搜索按钮
	search_button_xpath1 = '//div[@class="el-input-group__append"]'


	# 非监禁刑交付执行
	second_page_xpath = '//div[@id="tab-second"]'
	# 非监禁刑交付执行搜索文本框
	search_text_xpath2 = '//div[@id="pane-second"]//input[@placeholder="被执行人姓名/证件号"]'
	# 非监禁刑交付执行搜索结果条数
	search_res_xpath2 = '//div[@id="pane-second"]//span[@class="el-pagination__total"]'
	# 非监禁刑交付执行搜索按钮
	search_button_xpath2 = '//div[@id="pane-second"]//div[@class="el-input-group__append"]'