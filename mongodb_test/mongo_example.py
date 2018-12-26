#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 17:56
# @Author  : Kevindi
# @Site    : 
# @File    : mongo_example.py
# @Software: PyCharm Community Edition
# @Desc    :

# !/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]

dblist = myclient.list_database_names()
if "runoob" in dblist:
    print("数据库已存在！")

collist = mydb.list_collection_names()
if "mycol2" in collist:   # 判断 sites 集合是否存在
    print("集合已存在！")

user = {'name': 'Michael', 'age': 18, 'scores': [{'course': 'Math', 'score': 76}]}
result = mydb.mycol2.insert_one(user)
print('insert dir', dir(result))
print('insert ', result.inserted_id)

user = {'name': 'Tom', 'age': 21, 'scores': [{'course': 'Math', 'score': 85.5},
                                             {'course': 'Politics', 'score': 58}]}
user_id = mydb.mycol2.insert_one(user).inserted_id
print('Add user with id: %s' % user_id)


result = mydb.tests.insert_many([{'num': i} for i in range(3)])
print(result.inserted_ids)
