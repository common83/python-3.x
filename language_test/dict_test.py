#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 11:10
# @Author  : Kevindi
# @Site    : 
# @File    : dict_test.py.py
# @Software: PyCharm Community Edition
# @Desc    :

my_dict = {
    "a":0,
    "b":"b_value"
}
if type(my_dict) == type({}):
    print(my_dict.keys())

if 'a' in my_dict:
    print(my_dict['a'])

def func_A():
    print("A is here")

def func_B():
    print("B is here")

def func_C(value):
    print("C is ",value)

func_dic = {
    'a':func_A,
    'b':func_B,
    'c':func_C
}

func_dic['a']
func_dic['c']('cost')
func_dic['b']

jsonUI_data_json =  {'bHasMore': False, 'eAIRetCode': 0, 'eDisplayFormat': 3, 'eOptionalCmd': 0, 'ePlayMode': 0, 'eRetCode': 0, 'eSubService': 1, 'exstr': '', 'iContainCode': 1, 'sSpeak': '马上开始播放跨时代。', 'sText': '马上开始播放跨时代。'}
if 'sSpeak' in jsonUI_data_json:
    print('ddd=',jsonUI_data_json['sSpeak'])
