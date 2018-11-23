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