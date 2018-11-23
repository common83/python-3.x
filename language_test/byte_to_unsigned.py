#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 11:44
# @Author  : Kevindi
# @Site    : 
# @File    : byte_to_unsigned.py.py
# @Software: PyCharm Community Edition
# @Desc    :

slots = [ 6, 9, -25, -108, -100, -24, -100, -100, -24, -100, -100, 22, 9, -25, -108, -100, -24, -100, -100, -24, -100, -100, 32, 1 ]
for i in range(len(slots)):
    slots[i] = slots[i] & 0xff
print(slots)
