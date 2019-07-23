#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:42
# @Author  : fans
# @File    : Commutation_Parole_Case_Locators.py
# @Software: PyCharm Community Edition
class Commutation_Parole_Case_Locators:
	#用户名名称span   获取用户姓名
	# user_name_xpath='//span[@class="el-dropdown-link el-dropdown-selfdefine       "]'
	user_name_xpath='//div[@class="el-dropdown"]/span'
	#用户div   点击后可退出
	user_xpath='//div[@class="el-dropdown"]'
	#登出按钮
	log_out_button='//ul[@class="el-dropdown-menu el-popper"]'
	#确定按钮
	confirm_button='//div[@class="el-message-box__btns"]/button[2]'
	#搜索文本框
	search_text_xpath='//input[@placeholder="罪犯姓名/罪犯编号"]'
	#搜索结果条数
	search_res_xpath='//span[@class="el-pagination__total"]'
	#搜索按钮
	search_button_xpath='//div[@class="el-input-group__append"]'
	#新建案件按钮
	create_case_button_xpath='//span[contains(text(),"新建案件")]'
	#开始日期
	start_date='//input[@placeholder="开始日期"]'
	#结束日期
	end_date = '//input[@placeholder="结束日期"]'
	#案由
	case_type='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/form[1]/div[3]/div/div/input'
	case_type1='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/form[1]/div[3]/div/ul/li[1]'
	#筛选按钮
	choose_button='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/form[2]/div/div/button[1]'
	#重置按钮
	reset_button='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[2]/form[2]/div/div/button[2]'

	#第一个案件id
	# caseId2='//tbody/tr[@class="el-table__row hover-row"]//a'
	caseId = '//tbody/tr[@class="el-table__row hover-row"]//a'
	caseline = '//tbody/tr[@class="el-table__row"]//a'

	#减刑假释案件列表   上传按钮
	upload_button='//*[@id="app"]/div[2]/div[2]/div/div[1]/div/div[4]/div/div[5]/div[2]/table/tbody/tr/td[18]/div/button'
	# upload_button='//td[@class="el-table_3_column_54  "]//span'
	# upload_button='//button[@class="el-button el-button--primary el-button--small"]'
	#确定按钮
	upload_confirm_button='//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[3]/span/div/div/div'
	# upload_confirm_button='//button[@class="el-button el-button--primary el-button--medium"]'
	#上传成功提示
	upload_tip='//p[@class="el-message__content"]'


	#向前翻页
	button_prev='//button[@class="btn-prev"]'
	# 向后翻页
	button_next='//button[@class="btn-next"]'
	#页码按钮
	page_button='// li[text() = "2"]'
	#跳页按钮
	jump_button='//input[@type="number"]'