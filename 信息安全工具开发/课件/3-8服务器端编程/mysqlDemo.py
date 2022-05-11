import pymysql
#PyMySQL安装命令：pip3 install PyMySQL
# 安装成功后才能使用pymysql操作Mysql数据库
# 小扩展：如何快速注释和反注释：1.选中代码  2.按CTRL+？
#实验1： 查询数据库版本号
#打开数据库连接
# db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='TESTDB')
# #使用cursor(),方法创建一个游标对象
# cursor = db.cursor()
# #使用execute()执行SQL查询
# cursor.execute('SELECT VERSION()')
# #使用fetchone()获取单条数据
# data = cursor.fetchone()
# print("Database Version:%s" % data)
# #关闭数据库连接
# db.close()

#实验2.用Python创建数据库表
# db = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='TESTDB')
# cursor = db.cursor()
# #使用execute()执行SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# #构造创建数据表的SQL语句
# sql = "CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL," \
#       "LAST_NAME CHAR(20)," \
#       "AGE INT," \
#       "SEX CHAR(1)," \
#       "INCOME FLOAT)"
# #执行SQL语句
# cursor.execute(sql)
# #关闭连接
# db.close()

#实验3.向表EMPLOYEE插入数据
# db = pymysql.connect(host='localhost',user='root',password='123456',database='TESTDB')
# cursor = db.cursor()
# #sql语句的第一种写法
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) " \
#       "VALUES ('ZHAO','LIU',23,'M',3000.32)"
# #SQl语句的第二种写法 ?
# #sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('%s','%s',%s,'%s',%s) % ('li','si',22,'W',4000.86)"
# try:
#     #执行SQl语句
#     cursor.execute(sql)
#     #提交到数据库执行
#     db.commit()
# except:
#     #如果发生错误，则将数据库回滚到插入前的样子
#     db.rollback()
# #关闭连接
# db.close()

#实验4，查询
# db = pymysql.connect(host='localhost',user='root',password='123456',database='TESTDB')
# cursor = db.cursor()
# sql = "SELECT * FROM EMPLOYEE WHERE INCOME > 3000"
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         print("fname = %s,lname = %s,age= %s ,sex = %s,income = %s" % (fname,lname,age,sex,income))
# except:
#     print("Error")
# db.close()

#实验5，更新操作
# db = pymysql.connect(host='localhost',user='root',password='123456',database='TESTDB')
# cursor = db.cursor()
# #构建修改sql语句
# sql = "UPDATE EMPLOYEE SET INCOME = 4500 WHERE FIRST_NAME='WANG' AND LAST_NAME = 'WU'"
# try:
#     #执行SQL语句
#     cursor.execute(sql)
#     #提交给数据库执行
#     db.commit()
# except:
#     #出现错误回滚
#     db.rollback()
# db.close()

#实验6.删除操作
db = pymysql.connect(host='localhost',user='root',password='123456',database='TESTDB')
cursor = db.cursor()
#构建修改sql语句
sql = "DELETE FROM EMPLOYEE WHERE AGE < 22"
try:
    #执行SQL语句
    cursor.execute(sql)
    #提交给数据库执行
    db.commit()
except:
    #出现错误回滚
    db.rollback()
db.close()