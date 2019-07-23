#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 19:58
# @Author  : fans
# @File    : login_datas.py
# @Software: PyCharm Community Edition

#正常场景-测试数据
#司法局用户
sfj_account={"user":"sfj123","pwd":"123456"}
#安帮办用户
abb_account={"user":"sfj111","pwd":"123456"}
#监狱综治办用户
jy_account={"user":"sfj222","pwd":"123456"}
#司法局领导
jy_account={"user":"sfj333","pwd":"123456"}


#异常场景-未注册的用户、用户名或者密码错误、用户名为空、密码为空
wrong_datas=[
	{"user":"sfj999","pwd":"123456","check":"用户名或者密码错误！"},
	{"user":"sfj123","pwd":"999999","check":"用户名或者密码错误！"},
	{"user":"","pwd":"123456","check":"请输入用户名！"},
	{"user":"sfj123","pwd":"","check":"请输入密码！"}
]