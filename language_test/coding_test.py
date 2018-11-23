#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 11:01
# @Author  : Kevindi
# @Site    : 
# @File    : coding_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :
import urllib
from urllib import parse

test_t = '俄罗斯队的主教练'
text = '%B6%ED%C2%DE%CB%B9%B6%D3%B5%C4%D6%F7%BD%CC%C1%B7'
print('test_t=',test_t)
print('test=',text)
print('utf-8 = ', test_t.encode('GBK'))

print('utf-8 = ', parse.quote(test_t.encode('GBK')))

