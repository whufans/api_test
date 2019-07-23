#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:52
# @Author  : fans
# @File    : constants.py
# @Software: PyCharm Community Edition
import  os,time
abs_path=os.path.abspath(__file__)

base_path=os.path.dirname(os.path.dirname(abs_path))

common_dir=os.path.dirname(abs_path)

PageLocators_dir=os.path.join(base_path,'PageLocators')
PageObjects_dir=os.path.join(base_path,'PageObjects')
TestCases_dir=os.path.join(base_path,'TestCases')
TestDatas_dir=os.path.join(base_path,'TestDatas')

# datas_dir=os.path.join(base_path,'datas')
# excel_path=os.path.join(datas_dir,'Webservice_Test.xlsx')
Outputs_dir=os.path.join(base_path,'Outputs')
logs_dir=os.path.join(Outputs_dir,'Logs')

reports_dir=os.path.join(Outputs_dir,'Reports')
now = time.strftime("%Y-%m-%d-%H-%M-%S")
report_name =  now + 'test_result.html'
reports_path=os.path.join(reports_dir,report_name)

screen_shoots_dir=os.path.join(Outputs_dir,'Screen_Shoots')
screen_shoot_name='发放'
screen_shoots_path=screen_shoots_dir+'\\'+screen_shoot_name+now+'.jpeg'

