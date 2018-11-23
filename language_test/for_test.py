#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:35
# @Author  : Kevindi
# @Site    : 
# @File    : for_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :
from hyper.common.headers import HTTPHeaderMap


def h2_safe_headers(headers):
    print('h2_safe_headers debug 1', headers)
    stripped = {
        i.lower().strip()
        for k, v in headers if k == 'connection'
        for i in v.split(',')
    }
    stripped.add('connection')
    print('h2_safe_headers debug',stripped)
    print('h2_safe_headers debug 2', headers)

    t_header = list(headers.iter_raw())
    print('t_header=',t_header)

    re_header = [header for header in headers if header[0] not in stripped]
    print('re_header=',re_header)
    return re_header


headers = HTTPHeaderMap([(b':method', b'GET'), (b':scheme', b'https'), (b':authority', b'tvstest.html5.qq.com'), (b':path', b'/ping'), (b'Accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), (b'Accept-Charset', b'utf-8'), (b'Accept-Language', b'zh-cn,zh;q=0.5'), (b'Connection', b'close'), (b'Q-UA', b'SDK=1.0.0001&PP=com.tencent.dingdang.screenspeaker&MO=dingdang&VN=1.1.181106.104&VIN=104&CHID=10002'), (b'User-Agent', b'dingdangApp/1.0.0'), (b'Host', b'tvstest.html5.qq.com'), (b'Content-Type', b'multipart/form-data; boundary=this-is-a-boundary'), (b'authorization', b'Bearer 0B7ED61FF942C4E2D90F80831A408207,QQOPEN,1105886239,47632D181949D54F191B536773562070,2b82efec-a77c-46cd-a2c2-8df9bbd1d1c3:b50fd5a7baa547188516fec1fb5e3348,10:08:07:06:00:01,13b0a9bd0005a6ad')])

h2_safe_headers(headers)