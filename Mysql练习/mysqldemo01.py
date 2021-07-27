import pymysql

#打开数据库连接，主机名或ip，用户名，密码，数据库名称
db = pymysql.connect(host="localhost",user="root",password="123456",database="abc")
#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
#使用execute()方法执行SQL查询
cursor.execute("select version()")
#使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("Database version : %s "% data)
#关闭数据库连接
db.close()
