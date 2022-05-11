# -!- coding: UTF-8 -!-
import flask
import json
from flask import request,Flask
from DBDemo import db

server = Flask(__name__)
@server.route('/login',methods=['POST'])
def login():
    params = request.args
    if params:
        username = params.get("username")
        password = params.get("password")
    if username and password:#判断用户名密码不为空
        sql = "select * from user where username = '%s' and password = '%s';" % (username,password)
        result = db.my_db(sql)
        if result:
            res = {"error_code":200,"msg":"登陆成功"}
        else:
            res = {"error_code": 3001, "msg": "用户名或者密码错误"}
    else:
        res = {"error_code": 3000, "msg": "用户名或者密码不能为空"}
    return json.dumps(res,ensure_ascii=False)

server.run(port=8808)#指定端口号