#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 10:43
# @Author  : Kevindi
# @Site    : 
# @File    : example_find.py
# @Software: PyCharm Community Edition
# @Desc    :
from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/runoob"
mongo = PyMongo(app)

@app.route('/user')
@app.route('/user/<string:name>')
def user(name=None):
    if name is None:
        users = mongo.db.mycol2.find()
        return render_template('users.html', users=users)
    else:
        user = mongo.db.mycol2.find_one({'name': name})
        if user is not None:
            return render_template('users.html', users=[user])
        else:
            return 'No user found!'

if __name__ == '__main__':
    app.run(port=5002, debug=True)