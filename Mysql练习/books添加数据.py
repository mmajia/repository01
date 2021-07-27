from a创建连接数据库 import db,cursor

#数据列表
data = [("零基础学Python","python","79.80","2018-5-20"),
        ("Python从入门到精通","python","69.80","2018-6-18"),
        ("零基础学PHP","PHP","69.80","2017-5-21"),
        ("PHP项目开发实战入门","PHP","79.80","2016-5-21"),
        ("零基础学Java","python","69.80","2017-5-21")]

try:
    #执行sql语句，executemany插入多条数据
    cursor.executemany("insert into books(name,category,price,publish_time) values (%s,%s,%s,%s)",data)
    db.commit()
except:
    #如果发生错误回滚
    db.rollback()
db.close()