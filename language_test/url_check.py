#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 16:36
# @Author  : Kevindi
# @Site    : 
# @File    : url_check.py.py
# @Software: PyCharm Community Edition
# @Desc    :

import requests

response = requests.get('http://isure.stream.qqmusic.qq.com/C400003bVCqX2SRdEW.m4a?guid=1234727204&vkey=074C465F9EF179CEAE7D2B5B1EDE47481894C2A60B59DA228FD755B4DDDFB74E5CC5B3A4EA602D8164B1C9A3508ADA9B3701AE1B92A42744&uin=&fromtag=50')
assert response.status_code < 400