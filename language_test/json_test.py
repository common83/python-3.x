#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 16:50
# @Author  : Kevindi
# @Site    : 
# @File    : json_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :

import json

post_data = "{\"bot_session\":\"\",\"log_id\":\"7758521\",\"request\":{\"bernard_level\":0,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\"你好\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"88888\"},\"bot_id\":3744,\"version\":\"2.0\"}"

print(post_data)
print(json.loads(post_data,encoding='utf-8'))

print(json.loads(post_data))