#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 10:40
# @Author  : Kevindi
# @Site    : 
# @File    : urllib_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :
import urllib.request

proxies = {
    'http': 'http://proxy.tencent.com:8080',
    'https': 'https://proxy.tencent.com:8080'
}

file_name = '1501079663161.jpg'
proxy_support = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

urllib.request.urlretrieve("http://file.tuling123.com/upload/image/xiaohua/20170726/1501079663161.jpg", file_name)
