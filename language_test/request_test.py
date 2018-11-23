#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 11:01
# @Author  : Kevindi
# @Site    : 
# @File    : request_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :
import requests

url = 'http://isure.stream.qqmusic.qq.com/C400004NGo7N4IAyxE.m4a?guid=2000001810&vkey' \
      '=1D10DCF7116D04F43F4DDDC3894F9BBA0ACBFF491D3E6146A08DDB7B60324DA3127C7F3D96D6B7BD484' \
      'F22A792EA3E8AC7CC182E39989B42&uin=&fromtag=50'

response = requests.get(url=url)
print(response.status_code)
print(response.reason)