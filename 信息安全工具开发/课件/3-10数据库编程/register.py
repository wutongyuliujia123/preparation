# -!- coding: UTF-8 -!-
import flask
import json
from flask import request,Flask
from DBDemo import db

app = Flask(__name__)
@app.route('/register',methods=['POST','GET'])
def add_user():
    params = request.args
    #print(params.get("username"))
    #print(params.get("password"))
    if params:
        username = params.get("username")
        password = params.get("password")
        sex = params.get("sex",'0')
        age = params.get("age")
        telephone = params.get("telephone")
        income = params.get("income",5000)
        sql = "select * from user where username = '%s';" % username
        result = db.my_db(sql)
        if result:
            res = {"error_code":1000,"msg":"用户名已存在"}
        else:
            sql = "insert into user (username,password,age,sex,telephone,income) " \
                  "values ('%s','%s','%s','%s','%s','%s');" % (username,password,age,sex,telephone,income)
            db.my_db(sql)
            res = {"error_code":200,"msg":"插入成功"}
    return json.dumps(res,ensure_ascii=False)
if __name__ == "__main__":
    app.run()