#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 15:54
# @Author  : Kevindi
# @Site    : 
# @File    : flask_sample.py
# @Software: PyCharm Community Edition
# @Desc    :
# coding:utf-8
from flask import Flask,render_template,request,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/DingDangDB"
mongo = PyMongo(app)


@app.route('/',methods = ['GET','POST'])
def home():
    print('request dir=',dir(request.form))
    print('request form=',  request.form.getlist)
    print('request form=',  request.form.keys)
    print('request form=',  request.form.values)
    if request.method == 'POST':
        username = request.form['username2']
        password = request.form['passwords']
        if username == "user" and password == "password":
            return render_template('sample_home.html',title_name = '[title] ok')
        else:
            message = "Failed Login"
            return render_template('sample_home.html', title_name='[title] retry')
    return render_template('sample_home.html',title_name = '[title] welcome')


@app.route('/service',methods = ['GET','POST'])
def service():
    if request.method == 'GET':
        # 测试数据库是否连接成功，如果成功就会返回Pymongo一个游标对象。
        onlines_users = mongo.db.users.find()
        return render_template('sample_service.html', onlines_users=onlines_users, title_name = '[mongo] welcome')
        # 如果想在Index.html文件里显示效果就要加入{{ onlines_users }}调用方法。
    elif request.method == 'POST':
        print('dlt_test request.form.keys()=',request.form.keys())
        for key in request.form.keys():
            print('key=',key)
        # 更新数据
        if 'username1' in request.form.keys():
            username_new = request.form['username1']
            password_new = request.form['password1']
            user = mongo.db.users
            username_db = user.find_one({"username":username_new})
            if username_db:
                username_db['password'] = password_new
                user.save(username_db)
                return "Update OK: " + username_db['username']
            else:
                return "Not found user!"
        elif 'username' in request.form.keys():
            # 新增数据
            username = request.form['username']
            password = request.form['password']
            user = mongo.db.users
            user.insert({"username":username, "password": password})
            if user:
                return "用户不存在！"
            else:
                return "Added User!"

    return 'service'

@app.route('/about')
def about():
    return 'about'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

if __name__ == '__main__':
    app.run(port=5000, debug=True)