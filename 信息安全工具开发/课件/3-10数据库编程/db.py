# -!- coding: UTF-8 -!-
import pymysql
def my_db(sql):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='TESTDB')
    cur = conn.cursor()#创建一个游标对象
    cur.execute(sql)#执行SQl语句
    res = cur.fetchall()#获取sql执行结果
    conn.commit()#提交给数据库
    cur.close()
    conn.close()
    return res

def rock():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='TESTDB')
    cur = conn.cursor()  # 创建一个游标对象
    # SQL删除记录语句

    sql = "DELETE FROM user WHERE username = '%s';" % ('zhaoliu')
    # 执行SQL语句
    cur.execute(sql)
    # 向数据库提交
    conn.commit()
    conn.rollback()

rock()

