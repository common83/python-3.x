#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 16:53
# @Author  : Kevindi
# @Site    : 
# @File    : basic_requests_example.py
# @Software: PyCharm Community Edition
# @Desc    :

def requests_post():
    import requests

    # Base URL being accessed
    url = 'http://httpbin.org/post'

    # Dictionary of query parameters (if any)
    parms = {
       'name1' : 'value1',
       'name2' : 'value2'
    }

    # Extra headers
    headers = {
        'User-agent' : 'none/ofyourbusiness',
        'Spam' : 'Eggs'
    }

    resp = requests.post(url, data=parms, headers=headers)

    # Decoded text returned by the request
    text = resp.text
    print('text=', text)

def requests_more():
    # head 请求的例子
    import requests

    resp = requests.head('http://www.python.org/index.html')

    status = resp.status_code
    last_modified = resp.headers['last-modified']
    content_type = resp.headers['content-type']
    content_length = resp.headers['content-length']


    # 登陆
    import requests
    resp = requests.get('http://pypi.python.org/pypi?:action=login',
                        auth=('user', 'password'))

    # 使用cookies
    import requests
    url = 'http://pypi.python.org/pypi'
    # First request
    resp1 = requests.get(url)

    # Second requests with cookies received on first requests
    resp2 = requests.get(url, cookies=resp1.cookies)

    # 上传文件
    import requests
    url = 'http://httpbin.org/post'
    files = {'file': ('data.csv', open('data.csv', 'rb'))}
    r = requests.post(url, files=files)

def json_test():
    import requests
    r = requests.get('http://httpbin.org/get?name=Dave&n=37',
                     headers = {'User-agent': 'goaway/1.0'})
    resp = r.json
    print("resp['headers']", resp['headers'])


if __name__ == '__main__':
    # requests_post()
    # requests_more()
    json_test()