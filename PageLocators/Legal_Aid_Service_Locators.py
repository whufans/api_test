#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:45
# @Author  : fans
# @File    : Legal_Aid_Service_Locators.py
# @Software: PyCharm Community Edition
class Legal_Aid_Service_Locators:
	#法律援助服务模块
	main_page_xpath = '//a[text()="法律援助服务"]'
	#搜索框
	search_text_xpath = '//input[@placeholder="请输入受援人姓名/案件承办人姓名"]'
	#搜索结果条数
	search_res_xpath = '//span[@class="el-pagination__total"]'
	#搜索按钮
	search_button_xpath = '//div[@class="el-input-group__append"]'

	# 向前翻页
	button_prev = '//button[@class="btn-prev"]'
	# 向后翻页
	button_next = '//button[@class="btn-next"]'
	# 页码按钮
	page_button = '// li[text() = "2"]'
	# 跳页按钮
	jump_button = '//input[@type="number"]'

	#详情按钮
	fh_button='//*[contains(text(),"已反馈")]/parent::td/following-sibling::td//button[2]'
	zz_button='//*[contains(text(),"已终止")]/parent::td/following-sibling::td//button[2]'
	sl_button='//*[contains(text(),"已受理")]/parent::td/following-sibling::td//button[2]'
	#回到案件列表
	case_list='//a[text()="律师援助请求"]'
	#上传文件按钮
	upload_button='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[4]/div[2]/div[1]/div/div/div/button'


	#法律援助服务文本框
	input1='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[1]/div[1]/div/div/input'
	input2='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[1]/div[2]/div/div/input'
	input3='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[2]/div[1]/div/div/input'
	input4='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[2]/div[2]/div/div/input'
	input5='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[3]/div/div/input'

	#提交按钮
	submit='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[6]/div/form/div[4]/div/button'


	#
	xq='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[9]/div/button[2]'
	#终止按钮
	end_button='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[4]/div/button'
	#终止原因
	end_textarea='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/form/div[2]/div/div[1]/textarea'
	#确认终止按钮
	confirm_end_button='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/form/div[3]/div/button[1]'

	#案件状态区域
	case_status='//*[@id="app"]/div[2]/div[2]/div/div/div/div/div[2]/div/span[2]'