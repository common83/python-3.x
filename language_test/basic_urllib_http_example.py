#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 15:07
# @Author  : Kevindi
# @Site    : 
# @File    : basic_urllib_http_example.py
# @Software: PyCharm Community Edition
# @Desc    :

def basic_urllib():
    # 使用底层的 urllib 访问一个 http 服务,get方法
    from urllib import request,parse
    url = 'http://httpbin.org/get'

    # dirct of query params
    param = {
        'name1': 'value1',
        'name2': 'value2'
    }

    # encode the query string
    query_string = parse.urlencode(param)

    # Make a get request and read the response

    con = request.urlopen(url + '?' + query_string)
    resp = con.read()
    print('resp=',resp)

def basic_urllib_post():
    # 使用底层的 urllib 访问一个 http 服务,get方法
    from urllib import request,parse
    url = 'http://httpbin.org/post'

    # dirct of query params
    param = {
        'name1': 'value1',
        'name2': 'value2'
    }

    # encode the query string
    query_string = parse.urlencode(param)

    # Make a get request and read the response

    con = request.urlopen(url, query_string.encode('ascii'))
    resp = con.read()
    print('resp=',resp)

def basic_urllib_post_with_head():
    from urllib import request, parse
    # 需要设置 http 头，可以创建一个 Request 实例，再传给 urlopen

    url = 'http://httpbin.org/post'
    # dirct of query params
    param = {
        'name1': 'value1',
        'name2': 'value2'
    }

    # encode the query string
    query_string = parse.urlencode(param)

    # Extra headers
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }

    req = request.Request(url, query_string.encode('ascii'), headers=headers)

    # Make a request and read the response
    u = request.urlopen(req)
    resp = u.text
    print('resp=',resp)


if __name__ == '__main__':
    # basic_urllib()
    # basic_urllib_post
    basic_urllib_post_with_head()