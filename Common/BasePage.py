#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 16:12
# @Author  : fans
# @File    : BasePage.py
# @Software: PyCharm Community Edition
import inspect
import logging
import time
import win32gui
import win32con
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Common.Mylogger import MyLog
from Common import constants


def get__function_name():
	'''获取正在运行函数(或方法)名称'''
	return inspect.stack()[1][3]

class BasePage:
	def __init__(self,driver):
		self.driver=driver

	#   打开页面,并校验链接是否加载正确
	def _open(self, url):
		MyLog.info("正在打开网页:{}".format(url))
		MyLog.info("类名:{}  函数名:{}  正在打开网页:{}".format(self.__class__.__name__,get__function_name(),url))
		try:
			self.driver.get(url)
		except Exception as e :
			MyLog.error('{}未能正确打开页面{}' .format(self,url))
			raise  e

	# 等待元素可见
	def wait_eleVisible(self, loc,model_name="Screen_Shoot",by = By.XPATH ,timeout=20,poll_frequency=0.5):
		MyLog.info("等待元素可见:{}".format(loc))
		try:
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((by,loc)))
		except:
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise
		# except TimeoutException as  e:
		# 	MyLog.error("时间超时")
		# 	self.save_error_img(model_name)
		# 	raise  e
		# except  InvalidSelectorException as  e:
		# 	MyLog.error("元素定位表达式:{}不正确，请修正".format(loc))
		# 	self.save_error_img(model_name)
		# 	raise e

	#等待元素可点击
	def wait_eleClickable(self,loc,model_name="Screen_Shoot",by=By.XPATH,timeout=20,poll_frequency=0.5):
		MyLog.info("等待元素可点击:{}".format(loc))
		try:
			WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable(by,loc))
		except TimeoutException as  e:
			MyLog.error("时间超时")
			self.save_error_img(model_name)
			raise e
		except  InvalidSelectorException as  e:
			MyLog.error("元素定位表达式:{}不正确，请修正".format(loc))
			self.save_error_img(model_name)
			raise e

	#查找元素
	def find_element(self,loc,model_name="Screen_Shoot",by = By.XPATH):
		MyLog.info("正在查找元素:{}".format(loc))
		self.wait_eleVisible(loc,model_name)
		try:
			return self.driver.find_element(by,loc)
		except  NoSuchElementException as  e:
			MyLog.error("元素查找失败，找不到该元素。开始截取页面图像")
			self.save_error_img(model_name)
			raise e

	#点击元素
	def click_element(self,loc,model_name="Screen_Shoot"):
		ele=self.find_element(loc,model_name)
		try:
			ele.click()
		except :
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise

	#清除文本框内文本内容
	def clear_ele(self,loc,model_name="Screen_Shoot"):
		ele = self.find_element(loc, model_name)
		try:
			ele.clear()
		except :
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise

	# 定义script方法，用于执行js脚本，范围执行结果
	def script(self, src):
		self.driver.execute_script(src)

	# 重写定义send_keys方法  输入文本内容
	def input_text(self, loc, value,model_name="Screen_Shoot"):
		ele = self.find_element(loc, model_name)
		try:
			ele.send_keys(value)
		except:
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise

	#获取标题
	def get_title(self):
		return self.driver.title

	#获取元素文本内容
	def get_element_text(self,loc,model_name="Screen_Shoot",by = By.XPATH):
		MyLog.info("正在查找元素:{}".format(loc))
		ele = self.find_element(loc, model_name)
		try:
			return ele.text
		except :
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise

	#获取元素属性
	def get_element_attribute(self,loc,attr,model_name="Screen_Shoot",by = By.XPATH):
		MyLog.info("正在查找元素:{}".format(loc))
		ele = self.find_element(loc, model_name)
		try:
			return ele.get_attribute(attr)
		except :
			print("{}页面中未能找到{}元素".format(self, loc))
			self.save_error_img(model_name)
			raise

	#截图
	def save_error_img(self,model_name):
		try:
			# file_name=self.__class__.__name__+get__function_name()
			# screen_shoot_name ='\\'+ file_name + constants.now + '.png'
			file_path= constants.screen_shoots_dir + "/{}_{}.png".format(model_name, constants.now)
			self.driver.save_screenshot(file_path)
		except :
			logging.info("截图失败")

	#上传文件操作    窗口名称为打开
	def  upload(self,file):
		dialog = win32gui.FindWindow('#32770','打开')  # 找到windows对话框参数是（className，title）
		ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
		ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
		Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
		# 上面3句依次找对象，直到找出输入框Edit对象的句柄
		button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')  # 确定按钮
		# 跟上面示例的代码是一样的，只是这里传入的参数不同，如果愿意可以写一个上传函数把上传功能封装起来
		win32gui.SendMessage(Edit,win32con.WM_SETTEXT, 0, file)
		win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)



	# 重写switch_frame方法  切换到iframe
	def switch_frame(self):
		try:
			WebDriverWait(self.driver,20,0.5).until(EC.frame_to_be_available_and_switch_to_it)
			time.sleep(0.5)
		except :
			MyLog.error("未出现新的iframe。")

	#切换窗口
	def switch_window(self,index='-1'):
		handles=self.driver.window_handles
		try:
			WebDriverWait(self.driver,20,0.5).until(EC.new_window_is_opened(handles))
		except:
			MyLog.error("未出现新的窗口。")
		handles = self.driver.window_handles
		if index=='-1':
			self.driver.switch_to.window(handles[-1])
		elif index != None and  0<= int(index) <len(handles):
			self.driver.switch_to.window(handles[index])

	#切换到alert,点击确定或者取消
	def alert_handle(self,action="accept"):
		WebDriverWait(self.driver,20,0.5).until(EC.alert_is_present)
		alert=self.driver.switch_to.alert
		message=alert.text
		if action=="accept":
			alert.accept()
		else:
			alert.dismiss()
		return message

	def wait_until_page_contains_element(self,locator):
		pass

	def page_should_contain_element(self,locator):
		flag=True
		try:
			ele=self.find_element(locator)
			return flag
		except :
			flag=False
			return flag




