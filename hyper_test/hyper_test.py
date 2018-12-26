#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 15:24
# @Author  : Kevindi
# @Site    : 
# @File    : hyper_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :
from hyper import HTTPConnection

# 输入HTTP 2.0 的返回结果
def log_result(resp):
    print('resp=',resp)
    print('headers=',resp.headers['content-type'])
    print('headers=',resp.headers)
    print('status=',resp.status)
    print('read=',resp.read())

c = HTTPConnection('dueros-h2.baidu.com:443')
first = c.request('GET', '/')
s = c.request('POST', '/dcs/v1/')
t = c.request('GET', '/dcs/v1/')
print('ret=',first)
resp1 = c.get_response(first)
log_result(resp1)
resps = c.get_response(s)
log_result(resps)
respt = c.get_response(t)
log_result(respt)


