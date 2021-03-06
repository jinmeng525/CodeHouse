#-*- coding: utf-8 -*-
#python2.7x
#author: orangleliu@gmail.com 2014-12-25
#hello_script.py
'''
flask 只提供了web框架的核心功能，其他很多功能需要通过拓展来实现
这是falsk拓展的一个小案例
使用了flask_script拓展
'''

from flask import Flask
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)

#访问根目录，显示你好
@app.route("/")
def index():
    return '<h1> Hi  Flask</h1>'

#路由中可以自动正则匹配出值，对于restful应用很友好
@app.route("/user/<name>")
def user(name):
    return 'Hello %s'%name

if __name__ == '__main__':
    manager.run()

'''
PS D:\CodeHouse\flask\simple> python .\hello_script.py runserver
 * Running on http://127.0.0.1:5000/
'''
