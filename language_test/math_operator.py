#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 19:19
# @Author  : Aries
# @Site    : 
# @File    : math_operator.py.py
# @Software: PyCharm Community Edition

import math

a = math.log(8, 2)
print(a)
a = int(math.log(12,2))
print(a)

a = int(math.log(1,2))
print(a)

def point_data(a_list):
    for i in range(len(a_list)):
        a_list[i] = 3


a_list = [0,1,2,3,4,5,6]

point_data(a_list)
print(a_list)
